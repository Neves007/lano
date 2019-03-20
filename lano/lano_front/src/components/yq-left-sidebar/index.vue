<template>
    <div class="yq-siderbar-component" ref="card">
        <yq-sidebar-add @openPlanCreate="openPlanCreate" @getGroups="getGroups"></yq-sidebar-add>
        <yq-sidebar-collapse :file_name="title" :plan_list="plan_list" :groups="groups" :plans="plans"
                             @modifCurrentPlan="modifCurrentPlan" @changeToEditPlan="changeToEditPlan"></yq-sidebar-collapse>
    </div>
</template>

<script>
    // 组件
    import yqSidebarCollapse from './components/yq-siderbar-collapse.vue'
    import yqSidebarAdd from './components/yq-sidebar-add.vue'
    import axios from 'axios'
    let base_url = 'http://127.0.0.1:8000/';

    export default {
        name: 'yq-left-sidebar',
        data() {
            return {
                title: '舆情监测方案',
                plan_list: {},
                currentPlan: '',
                successToCreateGroup: false
            }
        },

        components: {
            'yq-sidebar-collapse': yqSidebarCollapse,
            'yq-sidebar-add': yqSidebarAdd,
        },
        props: {
            groups:{},
            plans: {},
            plan_list: {},
            // 容器样式
            type: {
                type: String,
                required: false,
                default: 'full'
            },
            // 滚动优化
            betterScroll: {
                type: Boolean,
                required: false,
                default: false
            },
            currentPlan: {}

        },
        methods: {
            modifCurrentPlan(cp){
                this.$emit('modifCurrentPlan',cp);
            },
            getGroups() {
                this.$emit('getGroups')
            },
            openPlanCreate() {
                this.$emit('openPlanCreate')
            },
            changeToEditPlan() {
                this.$emit('changeToEditPlan')
            }

        },
    }
</script>
