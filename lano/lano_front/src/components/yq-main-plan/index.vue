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
            <yq-main-plan-fast-create :show-fast="showFast"          :groupid="groupid"  @getPlans="getPlans"></yq-main-plan-fast-create>
            <yq-main-plan-advance-create :show-advance="showAdvance" :groupid="groupid" @getPlans="getPlans" ></yq-main-plan-advance-create>
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
                // plans:{},
                groups:[],
                show: false,
                show_setting: false,
                type: '快速',
                form_title: '高级',
                showFast:false,
                showAdvance:true,
                currentPlan: {fields:{
                    fast_name:'',
                    fast_area:'',
                    fast_character:'',
                    fast_event:'',
                    fast_exclude:'',
                    ad_name:'',
                    ad_match:'',
                    ad_exclude:'',
                    }},
                groupid:'',
                }
        },

        methods:{
            getGroups(){
                this.$emit('getGroups')
            },
            getPlans(){
                // this.plans=plans
                this.$emit('getPlans')
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
