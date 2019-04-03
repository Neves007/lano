<template>
    <div>
        <el-collapse class="cu_plan_collapse" v-model="collapseActiveName" Consistency>
            <el-collapse-item :key="index" v-for="(gp,index) in groups">
                <template slot="title" >
                    <span style="margin-left: 5px;"><i class="fa fa-minus-circle" style="margin-right: 5px;" @click="open(gp.pk)"></i> {{gp.fields.name}}</span>
                </template>
                <el-row style="margin-bottom: 0" v-for="plan_item in plans" :key="plan_item.pk">
                    <el-button-group v-show="plan_item.fields.group_id==gp.pk">
                        <el-button id="1" plain @click="getCurrentPlan(plan_item.pk)"><i class="fa fa-wrench"></i>
                            {{plan_item.fields.ad_name}}{{plan_item.fields.fast_name}}
                        </el-button>
                    </el-button-group>
                </el-row>
            </el-collapse-item>
        </el-collapse>

        <yq-sider-delete-dialog :show.sync="show" :group_id="group_id" @getGroups="getGroups"></yq-sider-delete-dialog>
    </div>


</template>

<script>
    import axios from 'axios'
    import YqSiderDeleteDialog from "./yq-sider-delete-dialog";

    let base_url = 'http://127.0.0.1:8000/';

    export default {
        name: "yq-siderbar-collaspse",
        components: {YqSiderDeleteDialog},
        data() {
            return {
                show:false,
                group_id:'11',
                collapseActiveName: '1',
                // search_plan:'',
            }
        },
        props: ["file_name", "plan_list", 'currentPlan', 'plan_operations', 'groups', 'plans'],
        methods: {
            getGroups() {
                 this.$emit('getGroups');
            },
            open(id) {
                this.group_id = id;
                this.show = true;
                // this.$emit('groupid',this.groupid);
                console.log('groupidf',this.group_id)
            },
            getCurrentPlan(id) {
                // this.plan_operations = false;
                // this.activeName = 'first';
                for (let p in this.plans) {
                    if (this.plans[p].pk === id) {
                        this.currentPlan = this.plans[p]
                        // console.log('current plan %o',this.currentPlan)
                    }
                }
                // console.log('collapse currentPlan',this.currentPlan.fields)
                this.$emit('clickCurrentPlan',this.currentPlan);
            },
        },
    }
</script>

<style scoped>


</style>
