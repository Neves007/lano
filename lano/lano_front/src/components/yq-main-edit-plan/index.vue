<template>
    <div>
        <div class="new-plan-fast_header">
            <div style="margin-left: 25px;margin-top: 10px;margin-bottom: 10px; display: inline-block;">{{form_title}}配置</div>
        </div>
        <yq-main-edit-plan-fast-create ref="fast" :show-fast="showFast" :currentPlan="currentPlan"
                                       @changeToEditPlan="changeToEditPlan" @getPlans="getPlans"></yq-main-edit-plan-fast-create>
        <yq-main-edit-plan-advance-create :show-advance="showAdvance" :currentPlan="currentPlan"
                                          @changeToEditPlan="changeToEditPlan"
                                          @getPlans="getPlans"></yq-main-edit-plan-advance-create>
    </div>
</template>

<script>

    import YqMainEditPlanFastCreate from "./components/yq-main-edit-plan-fast-create";
    import YqMainEditPlanAdvanceCreate from "./components/yq-main-edit-plan-advance-create";

    export default {
        name: "yq-main-edit-plan",
        components: {YqMainEditPlanAdvanceCreate, YqMainEditPlanFastCreate},
        data() {
            return {
                type: '高级',
                form_title: '快速',
                showFast: true,
                showAdvance: false,
                currentPlan: {fields:{
                    fast_name:'',
                    fast_area:'',
                    fast_character:'',
                    fast_event:'',
                    fast_exclude:'',
                    ad_name:'',
                    ad_match:'',
                    ad_exclude:'',
                    }},

            }
        },

        methods: {
            changeToEditPlan(){
                this.$emit('changeToEditPlan')
            },
            clickCurrentplan(currentPlan){
                console.log('editplan知道点击了plan',currentPlan)
                this.currentPlan=currentPlan
                this. initEditPlan()
                setTimeout(()=>{
                    this.$refs.fast.showFastPlan()
                })
            },
            initEditPlan(){
                if (this.currentPlan.fields.ad_name != null) {
                    this.form_title = '高级'
                    this.showAdvance = true
                    this.showFast = false
                }
                else if(this.currentPlan.fields.fast_name != null){
                    this.form_title = '快速'
                    this.showAdvance = false
                    this.showFast = true
                }
            },
            getPlans() {
                this.$emit('getPlans')
            },
            getGroups() {
                console.log('222222222222')
                this.$emit('getGroups')
            },
            changeToEditPlan() {
                this.$emit('changeToEditPlan')
                this.$emit('getGroups')
            },
        },
        mounted() {
            console.log('子组件eidit plan 已经mounted')
        }
    }
</script>

<style scoped>
    .new-plan-fast_header {
        background-color: #f5f7fa;
        border-bottom: 3px solid orange;
    }
</style>
