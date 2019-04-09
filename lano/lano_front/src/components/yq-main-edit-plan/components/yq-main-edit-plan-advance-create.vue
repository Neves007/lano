<template>
    <el-form ref="form" :model="currentPlan" :rules="advanceRules" v-if="showAdvance" style="margin-top: 40px"
             label-position="left"
             label-width="200px">
        <el-row>
            <el-form-item label="方案名称">
                <el-input v-model="currentPlan.fields.ad_name" placeholder="请输入方案名称" style="width: 40%"></el-input>
            </el-form-item>
        </el-row>
        <el-row>
            <i class="el-icon-question new_plan" @click="openAdvanceTip"></i>
            <el-form-item label="匹配关键词" prop="match">
                <el-input type="textarea" :rows="3" placeholder="请输入匹配关键词" v-model="currentPlan.fields.ad_match"
                          ref="match_input"></el-input>
                <el-button size="mini" @click="add1"
                           style="background-color: #e5e9f2;padding: 5px 10px;font-size: large">+
                </el-button>
                <el-button size="mini" @click="or1"
                           style="background-color: #e5e9f2;padding: 5px 10px;font-size: large">|
                </el-button>
                <el-button size="mini" @click="left_bracket1"
                           style="background-color: #e5e9f2;padding: 5px 10px;font-size: large">(
                </el-button>
                <el-button size="mini" @click="right_bracket1"
                           style="background-color: #e5e9f2;padding: 5px 10px;font-size: large">)
                </el-button>
                <span>(注意：匹配关键字总数请保持在18字以内，已输入
                                        <strong style="color: red;">{{matchUsedCount}}</strong>个字，还可以输入
                                        <strong style="color: red;">{{matchMaxLength - matchUsedCount}}</strong>个字。）</span>
                <el-button size="mini" class="fa fa-podcast" plain style="float:right;margin-top: 5px;
                                    background-color: #ff8100;color: white;">
                    <span style="font-weight: bold;">引用方案</span>
                </el-button>
            </el-form-item>
        </el-row>
        <el-row>
            <i class="el-icon-question new_plan" @click="openAdvanceTip"></i>
            <el-form-item label="排除关键词" prop="except2">
                <el-input type="textarea" :rows="3" placeholder="请输入排除关键词" ref="except_input"
                          v-model="currentPlan.fields.ad_exclude"></el-input>
                <el-button size="mini" @click="add2"
                           style="background-color: #e5e9f2;padding: 5px 10px;font-size: large">+
                </el-button>
                <el-button size="mini" @click="or2"
                           style="background-color: #e5e9f2;padding: 5px 10px;font-size: large">|
                </el-button>
                <el-button size="mini" @click="left_bracket2"
                           style="background-color: #e5e9f2;padding: 5px 10px;font-size: large">(
                </el-button>
                <el-button size="mini" @click="right_bracket2"
                           style="background-color: #e5e9f2;padding: 5px 10px;font-size: large">)
                </el-button>
                <span>(注意：排除关键词只支持一层嵌套，排除关键词不超过1000个字，已输入
                                        <strong style="color: red;">{{except2UsedCount}}</strong>个字，还可以输入
                                        <strong style="color: red;">{{except2MaxLength - except2UsedCount}}</strong>个字。）</span>
                <el-button size="mini" class="fa fa-podcast" plain style="float:right;margin-top: 5px;
                                    background-color: #ff8100;color: white;">
                    <span style="font-weight: bold;">引用方案</span>
                </el-button>
            </el-form-item>
        </el-row>
        <el-row>
            <el-form-item style="text-align:center">
                <el-button class="save" @click="modifPlan">保存</el-button>
                <el-button class="delete" @click="deletePlan">删除</el-button>
                <!--<el-button id="cancel">取消</el-button>-->
            </el-form-item>
        </el-row>
    </el-form>
</template>

<script>
    import axios from 'axios'

    let base_url = 'http://127.0.0.1:8000/';
    export default {
        name: "yq-main-edit-plan-advance-create",
        data() {

            let matchValidate = (rule, value, callback) => {
                if (!value) {
                    return callback()
                }

                let len = value.length;
                if (len <= this.matchMaxLength) {
                    this.matchUsedCount = len
                } else {
                    this.matchUsedCount = this.matchMaxLength;
                    this.advance_form.match = value.substr(0, this.matchMaxLength)
                }
            };
            let except2Validate = (rule, value, callback) => {
                if (!value) {
                    return callback()
                }

                let len = value.length;
                if (len <= this.except2MaxLength) {
                    this.except2UsedCount = len
                } else {
                    this.except2UsedCount = this.except2MaxLength;
                    this.advance_form.except2 = value.substr(0, this.except2MaxLength)
                }
            };
            return {
                advance_form: {
                    name: '',
                    match: '',
                    except2: '',
                },
                matchUsedCount: 0,
                except2UsedCount: 0,
                matchMaxLength: 18,
                except2MaxLength: 1000,

                advanceRules: {
                    match: [
                        {validator: matchValidate, trigger: 'change'}
                    ],
                    except2: [
                        {validator: except2Validate, trigger: 'change'}
                    ]
                },

            }
        },
        props: ['showAdvance', 'currentPlan'],
        methods: {
            deletePlan(){
                console.log('planid',this.currentPlan.pk);
                axios.post(base_url + 'api/delete_plan',this.currentPlan.pk).then(r => {
                    if (r.data.error_num === 0) {
                        this.$message.success("方案删除成功")
                        this.$emit('changeToEditPlan')
                        this.$emit('getPlans')
                    } else {
                        console.log('传递失败',r.data.msg)
                        this.$message.error("方案删除错误")
                    }
                })
                this.visible=false;
            },
            modifPlan() {
                if (this.currentPlan.fields.ad_name === '') {
                    this.$message.error('please input plan name')
                    return
                }
                console.log('update_plans currrentPlan',this.currentPlan)
                axios.post(base_url + 'api/update_ad_plans', JSON.stringify(this.currentPlan)).then(r => {
                    if (r.data.error_num === 0) {
                        this.$message.success("方案修改成功")
                    } else {
                        console.log('传递失败', r.data.msg)
                        this.$message.error("方案修改错误")
                    }
                })
                this.$emit('changeToEditPlan')
            },
            openAdvanceTip() {
                this.$alert(
                    '<el-row style="position: relative;">' +
                    '<i class="fa fa-circle-o" style="position:absolute;top:5px;"></i>' +
                    '<p style="margin-left: 20px">“+”表示“并且”，“|”表示“或”。</p></el-row>' +
                    '<el-row style="position: relative;">' +
                    '<i class="fa fa-circle-o" style="position:absolute;top:5px;"></i>' +
                    '<p style="margin-left: 20px">什么情况下用“|”：</p>' +
                    '<p style="margin-left: 20px">如想关注北京或上海或广州的新闻，表达式为“北京|上海|广州”，表示文章中出现“北京”、' +
                    '“上海”、“广州”任意一个城市就能监测到。</p></el-row>' +
                    '<el-row style="position: relative;">' +
                    '<i class="fa fa-circle-o" style="position:absolute;top:5px;"></i>' +
                    '<p style="margin-left: 20px">什么情况下用“+”：</p>' +
                    '<p style="margin-left: 20px">如想关注北京车牌摇号的新闻，表达式为“北京+车牌摇号”，' +
                    '表示文章中同时出现“北京”和“车牌摇号”两个关键词才能监测到。</p></el-row>' +
                    '<el-row style="position: relative;">' +
                    '<i class="fa fa-circle-o" style="position:absolute;top:5px;"></i>' +
                    '<p style="margin-left: 20px">什么情况下同时用到“+”、“|”：</p>' +
                    '<p style="margin-left: 20px">如想关注上海世博会的新闻，由于“世博会”有可能被称为“世界博览会”，' +
                    '表达式为“上海+（世博会|世界博览会）”，表示文章中出现“上海”，同时出现“世博会”' +
                    '或者“世界博览会”中任意一个词，就能监测到；</p></el-row>' +
                    '<el-row style="position: relative;">' +
                    '<i class="fa fa-circle-o" style="position:absolute;top:5px;"></i>' +
                    '<p style="margin-left: 20px">什么情况下用到排除关键词：</p>' +
                    '<p style="margin-left: 20px">如想关注上海、北京、广州的新闻，但又不想看到内容中有“三室一厅”、' +
                    '“二室一厅”这种关键词的广告，可以使用排除关键词的方式。匹配关键词表达式“北京|上海|广州”' +
                    ' 排除关键词表达式“三室一厅|二室一厅”</p></el-row>',
                    '关键词表达式使用示例', {
                        dangerouslyUseHTMLString: true,
                        showConfirmButton: false,

                    })
            },
            add1() {
                this.$refs.match_input.value = this.$refs.match_input.value + '+';
                // console.log("matchinput=",this.$refs.match_input.value);
                this.currentPlan.fields.ad_match= this.$refs.match_input.value
            },

            or1() {
                this.$refs.match_input.value = this.$refs.match_input.value + '|';
                this.currentPlan.fields.ad_match= this.$refs.match_input.value
            },

            left_bracket1() {
                this.$refs.match_input.value = this.$refs.match_input.value + '(';
                this.currentPlan.fields.ad_match= this.$refs.match_input.value
            },

            right_bracket1() {
                this.$refs.match_input.value = this.$refs.match_input.value + ')';
                this.currentPlan.fields.ad_match= this.$refs.match_input.value
            },
            add2() {
                this.$refs.except_input.value = this.$refs.except_input.value + '+';
                 this.currentPlan.fields.ad_exclude= this.$refs.except_input.value
            },

            or2() {
                this.$refs.except_input.value = this.$refs.except_input.value + '|';
                this.currentPlan.fields.ad_exclude= this.$refs.except_input.value
            },
            left_bracket2() {
                this.$refs.except_input.value = this.$refs.except_input.value + '(';
                this.currentPlan.fields.ad_exclude= this.$refs.except_input.value
            },
            right_bracket2() {
                this.$refs.except_input.value = this.$refs.except_input.value + ')';
                this.currentPlan.fields.ad_exclude= this.$refs.except_input.value
            },
            new_plan_onSubmit2() {
                this.$alert('成功保存!')
                this.activeName = 'first'
            },

        }
    }
</script>

<style scoped>

</style>
