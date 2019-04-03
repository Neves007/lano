<template>
    <el-form ref="form" :model="fast_form" :rules="fastRules" v-if="showFast" style="margin-top: 40px"
             label-position="left"
             label-width="200px">
        <el-row>
            <el-form-item label="方案名称">
                <el-input v-model="fast_form.name" placeholder="请输入方案名称"
                          style="width: 40%"></el-input>
            </el-form-item>
        </el-row>

        <el-row>
            <i class="el-icon-question new_plan" @click="openLocationMsg"></i>
            <el-form-item label="地域关键词" prop="region">
                <el-input type="textarea" :rows="3" placeholder="请输入地域关键词"
                          v-model="fast_form.region"></el-input>
                <el-button icon="el-icon-plus" size="small"
                           style="background-color: #00bc00;color: white;margin-top: 5px">添加关键词
                </el-button>
                <span>(注意：匹配关键字总数请保持在18字以内，已输入
                                        <strong style="color: red;">{{regionUsedCount}}</strong>个字，还可以输入
                                        <strong style="color: red;">{{regionMaxLength - regionUsedCount}}</strong>个字。）</span>
                <el-row>
                    <span style="margin-right: 15px">地域关系：</span>
                    <el-radio v-model="new_radio1" label="1">或</el-radio>
                    <el-radio v-model="new_radio1" label="2">与</el-radio>
                </el-row>
            </el-form-item>
        </el-row>
        <el-row>
            <i class="el-icon-question new_plan" @click="openLocationMsg"></i>
            <el-form-item label="人物关键词">
                <el-input type="textarea" :rows="3" placeholder="请输入人物关键词"
                          v-model="fast_form.person"></el-input>
                <el-button icon="el-icon-plus" size="small"
                           style="background-color: #00bc00;color: white;margin-top: 5px">添加主体词
                </el-button>
                <el-row>
                    <span style="margin-right: 15px">人物关系：</span>
                    <el-radio v-model="new_radio2" label="1">或</el-radio>
                    <el-radio v-model="new_radio2" label="2">与</el-radio>
                </el-row>
            </el-form-item>
        </el-row>
        <el-row>
            <i class="el-icon-question new_plan" @click="openLocationMsg"></i>
            <el-form-item label="事件关键词">
                <el-input type="textarea" :rows="3" placeholder="请输入事件关键词"
                          v-model="fast_form.thing"></el-input>
                <el-button icon="el-icon-plus" size="small"
                           style="background-color: #00bc00;color: white;margin-top: 5px">添加关键词
                </el-button>
                <el-row>
                    <span style="margin-right: 15px">事件关系：</span>
                    <el-radio v-model="new_radio3" label="1">或</el-radio>
                    <el-radio v-model="new_radio3" label="2">与</el-radio>
                </el-row>
            </el-form-item>
        </el-row>
        <el-row>
            <i class="el-icon-question new_plan" @click="openLocationMsg"></i>
            <el-form-item label="排除关键词" prop="except">
                <el-input type="textarea" :rows="3" placeholder="请输入排除关键词"
                          v-model="fast_form.except"></el-input>
                <el-button icon="el-icon-plus" size="small"
                           style="background-color: #00bc00;color: white;margin-top: 5px">添加关键词
                </el-button>
                <span>(注意：排除关键词只支持或运算，不超过1000个字，已输入
                                        <strong style="color: red;">{{exceptUsedCount}}</strong>个字，还可以输入
                                        <strong style="color: red;">{{exceptMaxLength - exceptUsedCount}}</strong>个字。）</span>
            </el-form-item>
        </el-row>
        <el-row>
            <el-form-item>
                <el-button class="save" @click="savePlan">保存</el-button>
                <!--<el-button id="cancel">取消</el-button>-->
            </el-form-item>
        </el-row>
    </el-form>

</template>

<script>
    import axios from 'axios'
    import util from '../../../libs/util'

    let base_url = 'http://127.0.0.1:8000/';


    export default {
        name: "yq-main-plan-fast-create",
        data() {
            let regionValidate = (rule, value, callback) => {
                if (!value) {
                    return callback()
                }

                let len = value.length;
                if (len <= this.regionMaxLength) {
                    this.regionUsedCount = len
                } else {
                    this.regionUsedCount = this.regionMaxLength;
                    this.fast_form.region = value.substr(0, this.regionMaxLength)
                }
            };
            let exceptValidate = (rule, value, callback) => {
                if (!value) {
                    return callback()
                }

                let len = value.length;
                if (len <= this.exceptMaxLength) {
                    this.exceptUsedCount = len
                } else {
                    this.exceptUsedCount = this.exceptMaxLength;
                    this.fast_form.except = value.substr(0, this.exceptMaxLength)
                }
            };

            return {
                new_radio1: '1',
                new_radio2: '1',
                new_radio3: '1',
                plan: {
                    fast_name:'',
                    fast_area:'',
                    fast_character:'',
                    fast_event:'',
                    fast_exclude:'',
                    ad_name:'',
                    ad_match:'',
                    ad_exclude:'',
                    },
                fast_form: {
                    name: '',
                    region: '',
                    person: '',
                    thing: '',
                    except: '',
                },
                regionUsedCount: 0,
                exceptUsedCount: 0,
                regionMaxLength: 18,
                exceptMaxLength: 1000,

                fastRules: {
                    region: [
                        {validator: regionValidate, trigger: 'change'}
                    ],
                    except: [
                        {validator: exceptValidate, trigger: 'change'}
                    ],

                },
            }
        },
        props: ['showFast', 'groupid'],
        methods: {
             getPlans() {
                this.$emit('getPlans')
            },
            openLocationMsg() {
                this.$alert(
                    '<el-row style="position: relative;">' +
                    '<i class="fa fa-circle-o" style="position:absolute;top:4px;"></i>' +
                    '<p style="margin-left: 20px">地域、人物、事件三类都可输入多个关键词，关键词之间用' +
                    '<strong style="color: red">空格分开</strong>。三个类型都可以为空</p></el-row>' +
                    '<el-row style="position: relative;">' +
                    '<i class="fa fa-circle-o" style="position:absolute;top:4px;"></i>' +
                    '<p style="margin-left: 20px">每一类的多个关键词之间默认为' +
                    '<strong style="color: red">“或（或者）”</strong>的关系，也可以手动修改为' +
                    '<strong style="color: red">“与（并且）”</strong>的关系。</p></el-row>' +
                    '<el-row style="position: relative;">' +
                    '<i class="fa fa-circle-o" style="position:absolute;top:4px;"></i>' +
                    '<p style="margin-left: 20px">地域、人物、事件三个类型之间是<strong style="color: red">' +
                    '“与（并且）”</strong>的关系。例如：地域配置了“上海”，人物配置了“周某”，' +
                    '事件配置了“撞车”，只有同时满足这3个条件的文章才会被监测到。</p></el-row>',
                    '关键词表达式使用示例', {
                        dangerouslyUseHTMLString: true,
                        showConfirmButton: false,

                    })
            },
            createPlan() {
                const uuid = util.cookies.get('uuid')
                if (this.plan.fast_name === '') {
                    this.$message.error('please input plan name')
                    return
                }
                //将创建的这个分组传给后台入库
                axios.post(base_url + 'api/create_fast_plan', JSON.stringify({
                    'plan': this.plan,
                    'uuid': uuid
                })).then(r => {
                    if (r.data.error_num === 0) {
                        this.getPlans()  //that.plans 拿到
                        this.$message.success("方案添加成功")
                    } else {
                        console.log('fast传递失败', r.data.msg)
                        this.$message.error("方案添加错误")
                    }
                })
            },
            savePlan() {
                this.plan['group_id'] = this.groupid
                this.plan['fast_name'] = this.fast_form.name
                this.plan['fast_area'] = this.fast_form.region
                this.plan['fast_character'] = this.fast_form.person
                this.plan['fast_event'] = this.fast_form.thing
                this.plan['fast_exclude'] = this.fast_form.except
                this.createPlan()
                this.fast_form.name = ''
                this.fast_form.region = ''
                this.fast_form.person = ''
                this.fast_form.thing = ''
                this.fast_form.except = ''
            },

        }
    }
</script>

<style scoped>

</style>
