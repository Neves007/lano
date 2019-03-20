<template>
    <div>
        <div class="new-plan-fast_header">
            <div style="margin-left: 25px; display: inline-block;">{{form_title}}配置</div>
            <el-button type="text" style="display: inline-block; margin-left: 20px" @click="changeForm">
                切换到{{type}}配置
            </el-button>
        </div>
        <yq-main-edit-plan-fast-create :show-fast="showFast" @openInfolist="openInfolist"></yq-main-edit-plan-fast-create>
        <yq-main-edit-plan-advance-create :show-advance="showAdvance" :currentPlan="currentPlan"></yq-main-edit-plan-advance-create>
    </div>
</template>

<script>

    import YqMainEditPlanFastCreate from "./components/yq-main-edit-plan-fast-create";
    import YqMainEditPlanAdvanceCreate from "./components/yq-main-edit-plan-advance-create";
    export default {
        name: "yq-main-edit-plan",
        components: {YqMainEditPlanAdvanceCreate, YqMainEditPlanFastCreate},
        props: ['currentPlan'],
        data(){
            return{
                type: '高级',
                form_title: '快速',
                showFast:true,
                showAdvance:false,
                currentPlan: {},

            }
        },

        methods:{
            changeForm() {
                if (this.type === '高级') {
                    this.showFast = false;
                    this.showAdvance = true;
                    this.type = '快速';
                    this.form_title = '高级'
                }
                else {
                    this.showFast = true;
                    this.showAdvance = false;
                    this.type = '高级';
                    this.form_title = '快速'
                }
            },
            openInfolist(){
                this.$emit('openInfolist')
            }
        }
    }
</script>

<style scoped>
    .new-plan-fast_header {
        background-color: #f5f7fa;
        border-bottom: 3px solid orange;
    }
</style>
