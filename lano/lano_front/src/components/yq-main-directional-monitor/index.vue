<template>
    <div>
        <div>
            <el-collapse class="cu_directional_collapse" v-model="directionCollapseName"
                         @change="handleChange">
                <!--<el-card class="cu_directional_card">-->
                    <!--<el-collapse-item name="1">-->
                        <!--<template slot="title">-->
                            <!--<span style="margin-left: 20px;font-size: medium">行业分类</span>-->
                        <!--</template>-->
                        <!--<yq-profession-classification></yq-profession-classification>-->
                    <!--</el-collapse-item>-->
                <!--</el-card>-->

                <el-card class="cu_directional_card">
                    <el-collapse-item name="2">
                        <template slot="title">
                            <span ref="monitor" style="margin-left: 20px;font-size: medium">定向监测</span>
                        </template>
                        <yq-directional-monitor ref="monitor" :currentPlan="currentPlan"></yq-directional-monitor>
                    </el-collapse-item>
                </el-card>

                <el-card class="cu_directional_card">
                    <el-collapse-item name="3">
                        <template slot="title">
                            <span style="margin-left: 20px;font-size: medium">定向排除</span>
                        </template>
                        <yq-directional-exclude ref="exclude" :currentPlan="currentPlan"></yq-directional-exclude>
                    </el-collapse-item>
                </el-card>
            </el-collapse>
        </div>
    </div>


</template>

<script>
    import YqProfessionClassification from "./componets/yq-profession-classification";
    import YqDirectionalMonitor from "./componets/yq-directional-monitor";
    import YqDirectionalExclude from "./componets/yq-directional-exclude";
    export default {
        name: "yq-main-directional-monitor",
        components: {YqDirectionalExclude, YqDirectionalMonitor, YqProfessionClassification},
        props: ['currentPlan'],
        data() {
            return{
                directionCollapseName: ['1', '2', '3'],
                currentPlan: {},
            }
        },
        methods:{
            directional_domain_handleCheckAllChange(val) {
                this.directional_data.domain_checked = val ? directional_domain_Options : []
                this.directional_data.isIndeterminate = false
            },
            directional_domain_handleCheckedCitiesChange(value) {
                let checkedCount = value.length
                this.directional_data.domain_checkAll = checkedCount === this.directional_data.domainOptions.length
                this.directional_data.isIndeterminate = checkedCount > 0 && checkedCount < this.directional_data.domainOptions.length
            },
            direction(){
                this.$refs.monitor.getDomainList();
                this.$refs.monitor.getWeiboList();
                this.$refs.monitor.getWechatList();
                this.$refs.exclude.getExDomainList();
                this.$refs.exclude.getExWeiboList();
                this.$refs.exclude.getExWechatList();
            }
        }
    }
</script>

<style scoped>

</style>