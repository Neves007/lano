<template>
    <d2-container :filename="filename">
        <el-row :gutter="10">
            <el-col :span="asideSpan">
                <el-card shadow="never">
                    <yq-left-sidebar ref="leftSidebar" :plan_list="plan_list" :currentPlan='currentPlan' :plans="plans"
                                     :groups="groups"
                                     @getGroups="getGroups"
                                     @openPlanCreate="openPlanCreate"
                                     @clickCurrentPlan="clickCurrentPlan"></yq-left-sidebar>
                </el-card>
            </el-col>
            <el-col :span="mainContentSpan">
                <div class="bg-purple-light" style="margin-bottom: 10px; padding: 10px"><b>{{currentPlan.fields.name}}</b></div>
                <el-tabs v-model="activeName" @tab-click="handleClick" type="border-card">
                    <el-tab-pane label="信息列表" name="first">
                        <yq-main-infolist :infolist="infolist" :infolist_count="infolist_count" :currentPlan="currentPlan" @getInfoList="getInfoList" @emitFilterData="filtInfolist"></yq-main-infolist>
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
                        <yq-main-plan @openInfolist="openInfolist" @getPlans="getPlans" @getGroups="getGroups"
                                      :groups="groups"></yq-main-plan>
                    </el-tab-pane>
                    <el-tab-pane label="修改方案" v-else name="eighth">
                        <yq-main-edit-plan :currentPlan="currentPlan" @changeToEditPlan="changeToEditPlan"
                                           @getPlans="getPlans"></yq-main-edit-plan>
                    </el-tab-pane>
                </el-tabs>
            </el-col>
        </el-row>
    </d2-container>
</template>

<script>

    import D2ContainerCard from '../../components/d2-container/components/d2-container-card'
    import axios from 'axios'
    import util from '../../libs/util.js'


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
                filter_data: {},
                groups: {},
                plans: {},
                plan_operations: true,
                plan_list: [],
                activeName: 'first',
                currentPlan: {fields:{name:'initialplan'}},
                asideSpan: 4,
                mainContentSpan: 20,
                infolist: [],
                infolist_count:'',
            }
        },
        methods: {
            filtInfolist(filter_data){
                console.log('点击查询后的filterdata',filter_data);
                this.getInfoList(30,1,filter_data)
            },
            changeToEditPlan() {
                this.plan_operations = false;
                this.activeName = 'first'
                this.getGroups()
            },
            getGroups() {
                let that = this;
                let temple_list = [];
                let uuid = util.cookies.get('uuid')
                console.log('大index，请求分组传的uuid是多少',uuid)
                axios.post(base_url + 'api/get_groups', JSON.stringify({'uuid':uuid})).then((r) => {
                    if (r.data.error_num === 0) {
                        for (let i = 0; i < r.data.list.length; i++) {
                            temple_list[i] = r.data.list[i];
                        }
                        that.groups = temple_list; //拿到所有分组
                        this.$emit('emitGroups', this.groups)
                    }
                }).catch(err => {
                    console.log('group error %o', err)
                })
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
                        this.$emit('emitPlans', this.plans)                    }
                }).catch(err => {
                    console.log('group error %o', err)
                })
            },
            clickCurrentPlan(cp){
                this.modifCurrentPlan(cp);
                this.changeToEditPlan();
                this.filter_data={
                    time_range_radio: 1,
                    article_order_radio: 1,
                    result_show_radio: 1,
                    repost_weibo_radio: 1,
                    msg_region: '四川',
                    msg_region_radio: 2,
                    weibo_content_radio: 1,
                    source_website_radio: 1,
                    sensitive_attr_radio: 1,
                    similar_article_radio: 1,
                    related_method_radio: 1,
                    match_method_radio: 1,
                    source_type_checkList: ['微信'],
                    source_type_checkAll: false,
                    isIndeterminate: true,
                    time_value: '',
                };
                
                this.getInfoList(30,1,this.filter_data);
            },
            modifCurrentPlan(cp) {
                this.plan_operations = false;
                this.currentPlan = cp
            },
            changeToEditPlan() {
                this.plan_operations = false;
                this.activeName = 'first'
            },
            getCurrentPlan(id) {
                console.log('大 index 点击方案getCurrentPlan id %o', id)
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

            getInfoList(page_size, page_num, filter_data) {
                this.filter_data=filter_data;
                let that = this;
                let temple_list = [];
                axios.get(base_url + 'api/switch_get_infolist', {
                    params: {
                        page_size: page_size,
                        page_num: page_num,
                        filter_data: filter_data,
                        current_plan: this.currentPlan,
                    }
                }).then((r) => {
                    if (r.data.error_num === 0) {
                        this.infolist=r.data.list;
                        console.log("大index中返回当前页面的infolist",this.infolist)
                        for (let i = 0; i < this.infolist.length; i++) {
                            temple_list[i] = r.data.list[i]['fields'];
                            // temple_list[i]['time'] = temple_list[i]['time'].replace("T", " ").replace("+08:00", "");
                            temple_list[i]['content'] = temple_list[i]['content'].replace(/<[^>]+>/g, "");
                            temple_list[i]['key_word'] = temple_list[i]['key_word'].replace(/@/g, "、");
                            temple_list[i]['type'] = temple_list[i]['type'];
                            temple_list[i]['content'] = temple_list[i]['content'].substring(0, 300);
                            temple_list[i]['id'] = i + 1;
                            // temple_list[i]['feelings'] = temple_list[i]['feelings'].toString();
                            temple_list[i]['warning_level'] = temple_list[i]['warning_level'].toString();
                        }
                        // that.infolist = temple_list;
                        that.infolist_count = r.data.list_count;
                    }
                }).catch(err => {
                    console.log('error %o', err)
                })
            },
        },


        mounted() {
            console.log("大index mouted的時候filter_data",this.filter_data)
            console.log("大index mouted的時候currentPlan",this.currentPlan)
        },

    }

</script>

<style scoped>
    @import "../../assets/style/page1/yuqing.scss";
</style>
