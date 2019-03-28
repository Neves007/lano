<template>
    <el-dialog title="删除分组" width="20%" center
                   :visible.sync="visible"
                   @close="$emit('update:show', false)"
                   :show="show">
        <span>
            要删除该分组及分组内所有方案吗？
        </span>
        <span slot="footer" class="dialog-footer">
            <el-button size="medium" class="cu_dialogBtn" @click="visible = false"
                   style="width: auto;display: inline-block;">取 消</el-button>
            <el-button size="medium" class="cu_dialogBtn" type="primary"
                   @click="deleteGroup"
                   style="width: auto;display: inline-block">确 定</el-button>
        </span>
    </el-dialog>
</template>

<script>
    import axios from 'axios'
    let base_url = 'http://127.0.0.1:8000/';

    export default {
        name: "yq-sider-delete-dialog",
        data() {
            return {
                visible: this.show,
            };
        },
        methods: {
            getGroups(){
                this.$emit('getGroups')
            },
            deleteGroup(){
                // console.log('groupidz',this.group_id)
                axios.post(base_url + 'api/delete_group',this.group_id).then(r => {
                    // console.log('groupid',group_id)
                    if (r.data.error_num === 0) {
                        this.getGroups();
                        this.$message.success("分组删除成功")
                    } else {
                        this.getGroups();
                        console.log('传递失败',r.data.msg)
                        this.$message.error("分组删除错误")
                    }
                })
                this.visible=false;
            },
            handleClose(done) {
                this.$confirm('确认关闭？')
                    .then(_ => {
                        done();
                    })
                    .catch(_ => {});
            }
        },
        props: {
            group_id:'',
            show: {
                type: Boolean,
                default: false
            }
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
