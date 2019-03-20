<template>
    <d2-container :filename="filename">
        <el-row :gutter="10">
            <el-col :span="asideSpan">
                <el-card shadow="never">
                    <yq-left-sidebar ref="leftSidebar" :plan_list="plan_list" :currentPlan='currentPlan' :plans="plans" :groups="groups"
                                     @getGroups="getGroups"
                                     @modifCurrentPlan='modifCurrentPlan'
                                     @openPlanCreate="openPlanCreate"
                                     @changeToEditPlan='changeToEditPlan'></yq-left-sidebar>
                </el-card>
            </el-col>
            <el-col :span="mainContentSpan">
                <div class="bg-purple-light" style="margin-bottom: 10px; padding: 10px"><b>{{currentPlan.name}}</b>
                </div>
                <el-tabs v-model="activeName" @tab-click="handleClick" type="border-card">
                    <el-tab-pane label="信息列表" name="first">
                        <yq-main-infolist></yq-main-infolist>
                    </el-tab-pane>
                    <el-tab-pane label="监测概述" name="collapse" style="background-color: #f8f8f9">
                        <el-row :gutter="30">
                            <!--地域分析-地图-->
                            <el-col :span="24">
                                <el-card shadow="hover" style="height: 813px">
                                    <div style="width: 100%; height: 794px; position: relative;">
                                        <div ref="ChinaMap" style="height: 500px;"></div>
                                    </div>
                                </el-card>
                            </el-col>
                        </el-row>
                    </el-tab-pane>
                    <el-tab-pane label="统计分析图" name="third">
                        <el-card class="bigCard" shadow="never">
                            <el-row :gutter="10">
                                <el-col :span='24'>
                                    <div ref="map" style="height: 500px;"></div>
                                </el-col>
                            </el-row>
                        </el-card>
                    </el-tab-pane>
                    <el-tab-pane label="精准设置" name="fourth">
                    </el-tab-pane>
                    <el-tab-pane label="定向监测" name="fifth">
                        <yq-main-directional-monitor></yq-main-directional-monitor>
                    </el-tab-pane>
                    <el-tab-pane label="预警设置" name="sixth">
                    </el-tab-pane>
                    <!--方案新建和修改tab-->
                    <el-tab-pane label="新建方案" v-if="plan_operations" name="seventh">
                        <yq-main-plan @openInfolist="openInfolist" @getPlans="getPlans" @getGroups="getGroups" :groups="groups"></yq-main-plan>
                    </el-tab-pane>
                    <el-tab-pane label="修改方案" v-else name="eighth">
                        <yq-main-edit-plan :currentPlan="currentPlan" @changeToEditPlan="changeToEditPlan" @getPlans="getPlans"></yq-main-edit-plan>
                    </el-tab-pane>
                </el-tabs>
            </el-col>
        </el-row>
    </d2-container>
</template>

<script>

    import D2ContainerCard from '../../components/d2-container/components/d2-container-card'
    import axios from 'axios'
    let base_url = 'http://127.0.0.1:8000/';


    import YqLeftSidebar from "../../components/yq-left-sidebar/index"
    import YqMainPlan from "../../components/yq-main-plan/index";
    import YqMainEditPlan from "../../components/yq-main-edit-plan/index";
    import YqMainDirectionalMonitor from "../../components/yq-main-directional-monitor/index";
    import YqMainInfolist from "../../components/yq-main-infolist/index";

    export default {
        name: 'page1',
        components: {
            YqMainInfolist,
            YqMainDirectionalMonitor, YqMainEditPlan, YqMainPlan, YqLeftSidebar, D2ContainerCard
        },

        data() {
            this.colors = ['#0694d6', '#e6a23a', '#61a0a8', '#d48265', '#91c7ae', '#749f83', '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3']

            return {
                groups:{},
                plans:{},
                plan_operations: true,
                plan_list: [],
                activeName: 'first',
                currentPlan: {},
                asideSpan: 4,
                mainContentSpan: 20,
            }
        },
        methods: {
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
            changeToEditPlan() {
                this.plan_operations = false;
                this.activeName = 'first'
                this.getGroups()
            },
            getGroups() {
                console.log('123')
                let that = this;
                let temple_list = [];
                axios.get(base_url + 'api/get_groups').then((r) => {
                    if (r.data.error_num === 0) {
                        for (let i = 0; i < r.data.list.length; i++) {
                            temple_list[i] = r.data.list[i];
                        }
                        console.log('大index收到mainplan的请求啦，现在要把把新的groups返回去',this.groups)
                        that.groups = temple_list; //拿到所有分组
                        this.$emit('emitGroups', this.groups)
                    }
                }).catch(err => {
                    console.log('group error %o', err)
                })
            },

            modifCurrentPlan(cp){
                this.plan_operations = false;
                this.currentPlan=cp
            },
            // emitPlans(plans){
            //    this.plans=plans
            // },
            getPlanList() {
                let that = this
                axios.get('/api/plan/plan_list').then((r) => {
                    if (r.data.code === 0) {
                        that.plan_list = r.data.plan
                        that.currentPlan = r.data.plan[0]
                    }
                }).catch(err => {
                    console.log('error %o', err)
                })
            },

            // getDomainList() {
            //     let that = this
            //     axios.get('/api/directional/domain_list').then((r) => {
            //         if (r.data.code === 0) {
            //             that.directional_data.dir_website_tableData = r.data.domain
            //         }
            //         console.log('response %o', r)
            //     }).catch(err => {
            //         console.log('error %o', err)
            //     })
            // },
            getCurrentPlan(id) {
                console.log('id %o', id)
                this.plan_operations = false
                this.activeName = 'first'
                for (var p in this.plan_list) {
                    if (this.plan_list[p].id === id) {
                        this.currentPlan = this.plan_list[p]
                    }
                }
            },
            openPlanCreate() {
                this.plan_operations = true;
                this.activeName = 'seventh'
            },
            changeToEditPlan() {
                this.plan_operations = false;
                this.activeName = 'first'
            },

        },

        mounted() {
            // this.getDomainList()
            this.getPlanList()
        },

    }

</script>

<style scoped>
    @import "../../assets/style/page1/yuqing.scss";
</style>
