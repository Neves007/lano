<template>
    <div>
        <el-dialog title="添加分组" width="30%" center
                   :visible.sync="visible"
                   @close="$emit('update:show', false)"
                   :show="show">
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
                                    style="margin-left: 10px;width: 70%;" v-model="group.name"></el-input>
                        </el-form-item>
                    </el-row>






                    <!--<div class="warning_header" style="margin-top: 20px">-->
                        <!--<div style="border-left: 4px solid orange;margin-top: 5px; display: inline-block;text-align: center">-->
                            <!--<span style="margin-left: 20px;font-size: small"><b>内容组</b></span>-->
                        <!--</div>-->
                    <!--</div>-->
                    <!--<el-row style="border-bottom: 1px solid #dcdfe6">-->
                        <!--<el-form-item label="创建时间：" style="margin-left: 20px;margin-top: 20px">-->
                            <!--<el-date-picker style="margin-left: 8px;width: 70%;"-->
                                            <!--type="datetime"-->
                                            <!--placeholder="选择日期时间"-->
                                            <!--align="right">-->
                            <!--</el-date-picker>-->
                        <!--</el-form-item>-->
                    <!--</el-row>-->
                    <!--<el-row style="border-bottom: 1px solid #dcdfe6">-->
                        <!--<el-form-item label="组名：" style="margin-left: 20px;margin-top: 20px">-->
                            <!--<el-input-->
                                    <!--style="margin-left: 10px;width: 70%;"></el-input>-->
                        <!--</el-form-item>-->
                    <!--</el-row>-->
                    <!--<el-row style="border-bottom: 1px solid #dcdfe6">-->
                        <!--<el-form-item label="APP显示名称：" style="margin-left: 20px;margin-top: 20px">-->
                            <!--<el-input-->
                                    <!--style="margin-left: 10px;width: 70%;"></el-input>-->
                        <!--</el-form-item>-->
                    <!--</el-row>-->
                </el-row>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button class="cu_dialogBtn" @click="close"
                       style="width: auto;display: inline-block;">取 消</el-button>
                <el-button class="cu_dialogBtn" type="primary"
                       @click="createGroup"
                       style="width: auto;display: inline-block">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    import YqSidebarAddGpForm from "./yq-sidebar-add-gp-form";
    import axios from 'axios'

    let base_url = 'http://127.0.0.1:8000/';
    export default {
        name: "yq-sidebar-add-gp-dialog",
        components: {YqSidebarAddGpForm},
        data() {
            return {
                groups: {},
                newGroupDialogVisible: false,
                visible: this.show,
                group: {
                    name: ''
                }
            }
        },
        methods: {
            getGroups() {
                 this.$emit('getGroups')
            },

            createGroup() {
                if (this.group.name === '') {
                    this.$message.error('please input group name')
                    return
                }
                //将创建的这个分组传给后台入库
                axios.post(base_url+'api/create_group', JSON.stringify(this.group)).then(r => {
                    if (r.data.error_num === 0) {
                        this.getGroups()  //新分组已入库，数据库需要重新读
                        this.show = false
                        this.group.name=''
                    } else {
                        this.$message.error("该分组已存在")
                    }
                })
            }
        },
        props: {
            show: {
                type: Boolean,
                default: false
            }
        },
        mounted() {
            this.getGroups();

        },
        watch: {
            show() {
                this.visible = this.show;
            }
        }
    }
</script>

<style scoped>

</style>
