<template>
    <div>
        <div class="new-plan-fast_header">
            <div style="margin-left: 25px; display: inline-block;">{{form_title}}配置</div>
            <el-button type="text" style="display: inline-block; margin-left: 20px" @click="changeForm">
                切换到{{type}}配置
            </el-button>
        </div>
        <el-row class="plan">
            <el-form ref="form" :rules="rules" label-position="left" label-width="200px">
                <el-form-item label="分组" style="margin-left: 0px;margin-top: 40px">
                    <el-select v-model="groupid" placeholder="请选择分组"
                            @change="showPlanSetting" >
                        <el-option
                            v-for="items in groups"
                            :key="items.fields.name"
                            :label="items.fields.name"
                            :value="items.pk">
                        </el-option>
                    </el-select>
                    <el-button icon="el-icon-plus" size="small" circle @click="open" style="margin-left: 10px"></el-button>
                    <!--<yq-sidebar-add-gp-dialog @getGroups="getGroups" :show.sync="show"></yq-sidebar-add-gp-dialog>-->
                </el-form-item>
            </el-form>
        </el-row>
        <yq-sidebar-add-gp-dialog @getGroups="getGroups" :show.sync="show"></yq-sidebar-add-gp-dialog>
        <div v-if="show_setting">
            <yq-main-plan-fast-create :show-fast="showFast" @openInfolist="openInfolist"></yq-main-plan-fast-create>
            <yq-main-plan-advance-create :show-advance="showAdvance" :groupid="groupid" @emitPlans="emitPlans"></yq-main-plan-advance-create>
        </div>
    </div>
</template>

<script>
    import YqMainPlanFastCreate from "./components/yq-main-plan-fast-create";
    import YqMainPlanAdvanceCreate from "./components/yq-main-plan-advance-create";
    import YqSidebarAddGpDialog from "./components/yq-sidebar-add-gp-dialog";
    import axios from 'axios'
    let base_url = 'http://127.0.0.1:8000/';

    export default {
        name: "yq-main-plan",
        props:['groups'],
        components: {
            'yq-sidebar-add-gp-dialog':YqSidebarAddGpDialog,
            'yq-main-plan-advance-create':YqMainPlanAdvanceCreate,
            'yq-main-plan-fast-create':YqMainPlanFastCreate
        },
        data(){
            return{
                plans:{},
                groups:[],
                show: false,
                show_setting: false,
                type: '高级',
                form_title: '快速',
                showFast:true,
                showAdvance:false,
                currentPlan: {},
                groupid:'',
                }
        },

        methods:{
            getGroups(){
                this.$emit('getGroups')
            },
            getPlans() {
                let that = this;
                let temple_list = [];
                axios.get(base_url + 'api/get_plans').then((r) => {
                    if (r.data.error_num === 0) {
                        for (let i = 0; i < r.data.list.length; i++) {
                            temple_list[i] = r.data.list[i];
                        }
                        that.plans = temple_list; //拿到所有分组
                        this.$emit('emitPlans',this.plans)

                    }
                }).catch(err => {
                    console.log('group error %o', err)
                })
            },
            emitPlans(plans){
                this.plans=plans
                this.$emit('emitPlans',this.plans)
            },
            open () {
                this.show = true;
            },
            showPlanSetting() {
                if (this.groupid !=='') {
                    this.show_setting = true
                }
                if (this.groupid === '') {
                    this.show_setting = false
                }
            },
            changeForm() {
                if (this.type === '高级') {
                    this.showFast = false;
                    this.showAdvance = true;
                    this.type = '快速';
                    this.form_title = '高级'
                }
                else {
                    this.showFast = true;
                    this.showAdvance = false;
                    this.type = '高级';
                    this.form_title = '快速'
                }
            },
            openInfolist(){
                this.$emit('openInfolist')
            }
        },
        mounted() {
            this.getPlans();
        }
    }
</script>

<style scoped>
    .new-plan-fast_header {
        background-color: #f5f7fa;
        border-bottom: 3px solid orange;
    }
</style>
