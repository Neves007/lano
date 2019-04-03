<template>
    <div>
        <yq-sidebar-add-gp-dialog @getGroups="getGroups" :show.sync="show"></yq-sidebar-add-gp-dialog>
        <el-row :gutter="8">
            <el-col :span='12'>
                <el-button type="warning" size="small" icon="el-icon-plus" plain
                           @click="open">
                    <span style="font-weight: bold;">添加分组</span>
                </el-button>
                <yq-sidebar-add-gp-dialog @getGroups="getGroups" :show.sync="show"></yq-sidebar-add-gp-dialog>
            </el-col>
            <el-col :span='12'>
                <el-button type="warning" size="small" icon="el-icon-plus" plain @click="openPlanCreate">
                    <span style="font-weight: bold;">添加方案</span>
                </el-button>
            </el-col>
            <el-col>
                <el-input style="padding: 8px 0" placeholder="搜索监测方案或文件夹"
                          prefix-icon="el-icon-search" v-model="search_plan"></el-input>
                <!--<el-button v-on:click="transferSearchMsg">搜索</el-button>-->
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import YqSidebarAddGpDialog from "./yq-sidebar-add-gp-dialog";
    // import bus from '../../../pages/message-summary/eventBus';

    export default {
        name: "yq-sidebar-add",
        components: {YqSidebarAddGpDialog},
        data() {
            return {
                show: false,
                // search_plan: ''
            }

        },
        methods: {

            getGroups() {
                this.$emit('getGroups')
            },
            open() {
                this.show = true;
            },
            openPlanCreate() {
                this.$emit('openPlanCreate')
            },
            // transferSearchMsg:function () {
            //     bus.$emit("searchPlanEvent",'test')
            // }
        },
    }
</script>

<style scoped>
    .el-button--warning {
        color: #e6a23c;
        background: white;
        border: 1px solid #e6a23c;

    }

    .el-button--warning :hover {
        background: #e6a23c;
        border-color: #e6a23c;
        color: #fff;
    }

    .el-button--warning :focus {
        background: #e6a23c;
        border-color: #e6a23c;
        color: #fff;
    }
</style>
