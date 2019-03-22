<template>
    <div>
        <yq-main-infolist-top ref="filterChild" @emitFilterData="emitFilterData"></yq-main-infolist-top>
        <br>
        <br>
        <div class="article">
            <table style="width: 100%;" cellspacing="0">
                <!--表头-->
                <thead>
                <tr>
                    <th colspan="3">标题</th>
                    <th style="white-space: nowrap;">相似文章数</th>
                    <th>来源</th>
                    <th>时间</th>
                </tr>
                </thead>
                <!--内容-->
                <yq-main-infolist-table :infolist_count="infolist_count" :infolist="infolist" @nextPage="nextPage"></yq-main-infolist-table>
            </table>
        </div>
    </div>

</template>

<script>
    import axios from 'axios'
    import Mock from 'mockjs'
    import YqMainInfolistTable from "./components/yq-main-infolist-table";
    import YqMainInfolistTop from "./components/yq-main-infolist-top";

    let base_url = 'http://127.0.0.1:8000/';
    export default {
        name: "yq-main-infolist",
        components: {YqMainInfolistTop, YqMainInfolistTable},
        data() {
            return {
                // flag: false,

            }
        },
        props:{
            infolist: [],
            infolist_count:'',
            currentPlan:{}
        },
        methods: {
            getInfoList(page_size, page_num, filter_data) {
                this.$emit("getInfoList",page_size, page_num, filter_data)
            },
            nextPage(page_num) {
                this.getInfoList(30, page_num, this.$refs.filterChild.infolist_filter)
            },


            emitFilterData(filter_data) {
                this.$emit("emitFilterData", filter_data)
            }
        },
        mounted() {
            this.getInfoList(30, 1,this.$refs.filterChild.infolist_filter);
        },

    }
</script>

<style scoped>
    @import "../../assets/style/page1/yuqing.scss";
</style>
