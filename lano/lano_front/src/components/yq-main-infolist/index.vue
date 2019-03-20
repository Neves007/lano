<template>
    <div>
        <yq-main-infolist-top ref="filterChild" @filterData="filterInfolist"></yq-main-infolist-top>
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
                <yq-main-infolist-table :list_count="infolist_count" :infolist="info_list" @nextPage="nextPage"></yq-main-infolist-table>
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
        // props:['info_list'],
        data() {
            return {
                // flag: false,
                info_list: [],
                infolist_count:''
            }
        },
        methods: {
            getInfoList(page_size, page_num, filter_data) {
                let that = this;
                let temple_list = [];
                axios.get(base_url + 'api/switch_get_infolist', {
                    params: {
                        page_size: page_size,
                        page_num: page_num,
                        filter_data:filter_data
                    }
                }).then((r) => {
                    if (r.data.error_num === 0) {
                        for (let i = 0; i < r.data.list.length; i++) {
                            temple_list[i] = r.data.list[i]['fields'];
                            // temple_list[i]['time'] = temple_list[i]['time'].replace("T", " ").replace("+08:00", "");
                            temple_list[i]['content'] = temple_list[i]['content'].replace(/<[^>]+>/g, "");
                            temple_list[i]['key_word'] = temple_list[i]['key_word'].replace(/@/g, "、");
                            temple_list[i]['type'] = temple_list[i]['type'];
                            temple_list[i]['content'] = temple_list[i]['content'].substring(1, 300);
                            temple_list[i]['id'] = i + 1;
                            // temple_list[i]['feelings'] = temple_list[i]['feelings'].toString();
                            temple_list[i]['warning_level'] = temple_list[i]['warning_level'].toString();
                        }
                        that.info_list = temple_list;
                        that.infolist_count = r.data.list_count;
                        // that.flag = true
                    }
                }).catch(err => {
                    console.log("是不是这儿错了")
                    console.log('error %o', err)
                })
            },

            nextPage(page_num) {
                this.getInfoList(30, page_num, this.$refs.filterChild.infolist_filter)
            },
            filterInfolist(filter_data) {
                this.getInfoList(30, 1, filter_data)
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
