<template>
    <el-form ref="form" :rules="rules"
             label-position="left" label-width="150px">
        <el-row class="warning_row">
            <div class="warning_header">
                <div style="border-left: 4px solid orange;margin-top: 5px; display: inline-block;text-align: center">
                    <span style="margin-left: 20px;font-size: small"><b>创建组</b></span>

                    <el-tooltip class="item" effect="dark" placement="right-end">
                        <div slot="content">内容组用于添加内容或监测方案，结构组用于管理内容组的层级
                            ，可分为多层级。<br/>例如：监控上海市各区公安局，可设为：上海市（结构组）——徐汇区/静安区...(内容组）——监测方案
                        </div>
                        <i class="el-icon-question" style="margin-left: 10px"></i>
                    </el-tooltip>
                </div>
            </div>
            <el-row style="border-bottom: 1px solid #dcdfe6">
                <el-form-item label="新建结构组/组名：" style="margin-left: 20px;margin-top: 20px">
                    <el-input
                              style="margin-left: 10px;width: 70%;"></el-input>
                </el-form-item>
            </el-row>




            <div class="warning_header" style="margin-top: 20px">
                <div style="border-left: 4px solid orange;margin-top: 5px; display: inline-block;text-align: center">
                    <span style="margin-left: 20px;font-size: small"><b>内容组</b></span>
                </div>
            </div>
            <el-row style="border-bottom: 1px solid #dcdfe6">
                <el-form-item label="创建时间：" style="margin-left: 20px;margin-top: 20px">
                    <el-date-picker style="margin-left: 8px"
                                    type="datetime"
                                    placeholder="选择日期时间"
                                    align="right"

                                    >
                    </el-date-picker>
                </el-form-item>
            </el-row>
            <el-row style="border-bottom: 1px solid #dcdfe6">
                <el-form-item label="组名：" style="margin-left: 20px;margin-top: 20px">
                    <el-input
                              style="margin-left: 10px;width: 70%;"></el-input>
                </el-form-item>
            </el-row>
            <el-row style="border-bottom: 1px solid #dcdfe6">
                <el-form-item label="APP显示名称：" style="margin-left: 20px;margin-top: 20px">
                    <el-input
                              style="margin-left: 10px;width: 70%;"></el-input>
                </el-form-item>
            </el-row>

        </el-row>

    </el-form>


</template>

<script>
    export default {
        name: "yq-sidebar-add-gp-form",

    }
</script>

<style scoped>

</style>
