<template>
    <div>
        <!--<el-row class="warning_row">-->
        <div class="warning_header">
            <div style="border-left: 4px solid orange;margin-top: 5px; display: inline-block;text-align: center">
                <span style="margin-left: 20px;font-size: small"><b>预警开关</b></span>
            </div>
        </div>
        <el-row>
            <span style="margin-left: 100px;margin-top: 20px">预警开关：</span>
            <!--<el-radio-group class="warning_radio" size="small" v-model="warning_open_radio" @change.native="showWarningSetting">-->
            <!--<el-radio class="warning_radio"-->
            <!--label="1"  border-->
            <!--style="margin-left: 10px;" >打开-->
            <!--</el-radio>-->
            <!--<el-radio class="warning_radio"-->
            <!--label="2" border>关闭-->
            <!--</el-radio>-->
            <!--</el-radio-group>-->
            <el-radio class="warning_radio" v-model="warning_open_radio"
                      label="1" size="small" border
                      style="margin-left: 10px;" @change="showWarningSetting">打开
            </el-radio>
            <el-radio class="warning_radio" v-model="warning_open_radio"
                      label="2" size="small" border @change="showWarningSetting">关闭
            </el-radio>
        </el-row>
        <yq-main-warning-setting :show_setting="show_warning_setting" :current-plan="currentPlan"></yq-main-warning-setting>
    </div>

</template>

<script>
    import YqMainWarningSetting from "./components/yq-main-warning-setting";

    export default {
        name: "yq-main-warning",
        components: {YqMainWarningSetting},
        props:['currentPlan'],
        data() {
            return {
                show_warning_setting: true,
                warning_open_radio: '1',
            }
        },
        method: {
            showWarningSetting() {
                if (this.warning_open_radio === '1') {
                    this.show_warning_setting = true
                }
                if (this.warning_open_radio === '2') {
                    this.show_warning_setting = false
                }
            },
        },

    }
</script>

<style>
    @import "../../assets/style/page1/yuqing.scss";
</style>