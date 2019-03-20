<template>
    <el-collapse class="cu_plan_collapse" v-model="collapseActiveName" Consistency>
        <el-collapse-item :key="index" v-for="(gp,index) in groups">
            <template slot="title" >
                <span style="margin-left: 5px;"><i class="fa fa-folder-open"></i> {{gp.fields.name}}
                    <i class="fa fa-minus-circle" ></i></span>

            </template>
            <el-row style="margin-bottom: 0" v-for="plan_item in plans" :key="plan_item.pk">
                <el-button-group v-show="plan_item.fields.group_id==gp.pk">
                    <el-button plain @click="getCurrentPlan(plan_item.pk)">
                        <i class="fa fa-wrench"></i>
                        {{plan_item.fields.name}}
                    </el-button>
                </el-button-group>
            </el-row>
        </el-collapse-item>

    </el-collapse>

</template>

<script>
    import axios from 'axios'

    let base_url = 'http://127.0.0.1:8000/';

    export default {
        name: "yq-siderbar-collaspse",
        data() {
            return {
                collapseActiveName: '1',
                // search_plan:'',
            }
        },
        props: ["file_name", "plan_list", 'currentPlan', 'plan_operations', 'groups', 'plans'],
        methods: {
            getCurrentPlan(id) {
                // this.plan_operations = false;
                // this.activeName = 'first';
                this.$emit('changeToEditPlan')
                for (let p in this.plans) {
                    if (this.plans[p].pk === id) {
                        this.currentPlan = this.plans[p]
                    }
                }
                this.$emit('modifCurrentPlan',this.currentPlan);
            },
        },
    }
</script>

<style scoped>
    .cu_plan_collapse >>> .el-collapse-item__wrap {
        will-change: height;
        overflow: hidden;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        border-bottom: 0 solid #ebeef5;
    }

    .cu_plan_collapse >>> .el-collapse-item__header {
        border-bottom: 0;
        border-top: 3px solid orange;
    }

    .el-button-group > .el-button:first-child:last-child {
        border-radius: 0;
        border: 0;
        border-left: 3px solid white;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        width: 260px;
        text-align: left;

    }

    .el-button-group > .el-button:first-child:last-child:hover {
        background: #eaeaea;
        color: orange;
    }

    .el-button-group > .el-button:first-child:last-child:focus {
        background: #eaeaea;
        border-left: 3px solid orange;
        color: orange;
    }

</style>
