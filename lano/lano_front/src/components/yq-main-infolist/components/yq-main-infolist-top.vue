<template>
    <div>
        <el-row class="shuxing" style="padding-left: 10px">
            <el-col :span="12">
                <!--时间范围-->
                <div style="font-size: 14px; display: inline-block">时间范围：</div>
                <el-radio-group v-model="infolist_filter.time_range_radio" class="cu_infolist_radio"
                                @change="zidingyishijian">
                    <el-radio :label=1>今日</el-radio>
                    <el-radio :label=2>24小时</el-radio>
                    <el-radio :label=3>2天</el-radio>
                    <el-radio :label=4>3天</el-radio>
                    <el-radio :label=5>7天</el-radio>
                    <el-radio :label=6>10天</el-radio>
                    <el-radio :label=7>自定义</el-radio>
                </el-radio-group>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                <!--文章排序-->
                <div style="font-size: 14px; display: inline-block">文章排序：</div>
                <el-radio-group v-model="infolist_filter.article_order_radio" class="cu_infolist_radio">
                    <el-radio :label=1>智能排序</el-radio>
                    <el-radio :label=2>时间降序</el-radio>
                    <el-radio :label=3>时间升序</el-radio>
                    <el-radio :label=4>相似文章</el-radio>
                    <el-radio :label=5>采集顺序</el-radio>
                </el-radio-group>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                <!--结果呈现-->
                <div style="font-size: 14px; display: inline-block">结果呈现：</div>
                <el-radio-group v-model="infolist_filter.result_show_radio" class="cu_infolist_radio">
                    <el-radio :label="1">正常信息</el-radio>
                    <el-radio :label="2">精准信息</el-radio>
                    <el-radio :label="3">疑似垃圾</el-radio>
                </el-radio-group>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                <!--转发微博-->
                <div style="font-size: 14px; display: inline-block">转发微博：</div>
                <el-radio-group v-model="infolist_filter.repost_weibo_radio" class="cu_infolist_radio">
                    <el-radio :label="1">显示</el-radio>
                    <el-radio :label="2">不显示</el-radio>
                </el-radio-group>
                <el-tooltip class="item" effect="dark" content="微博只对新浪微博生效" placement="right">
                    <i class="el-icon-question custom-helper-info"></i>
                </el-tooltip>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;margin-bottom: 4px;"/>
                <!--信源区域-->
                <div style="font-size: 14px; display: inline-block">信源区域：</div>
                <el-select class="xinyuanquyu" v-model="infolist_filter.msg_region" placeholder="全部" size="mini"
                           @change="xinyuanquyu">
                    <el-option
                            v-for="item in options"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
                <el-radio-group v-model="infolist_filter.msg_region_radio" class="cu_infolist_radio"
                                @change="xinyuanquyu_danxuan">
                    <el-radio :label="2">省内</el-radio>
                    <el-radio :label="3">省外</el-radio>
                </el-radio-group>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;margin-top: 4px;"/>
                <!--微博内容-->
                <div style="font-size: 14px; display: inline-block">微博内容：</div>
                <el-radio-group v-model="infolist_filter.weibo_content_radio" class="cu_infolist_radio">
                    <el-radio :label="1">全部</el-radio>
                    <el-radio :label="2">按文本</el-radio>
                    <el-radio :label="3">按图文</el-radio>
                    <el-radio :label="4">按视频</el-radio>
                    <el-radio :label="5">按短链</el-radio>
                </el-radio-group>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                <div style="font-size: 14px; display: inline-block">来源网站：</div>
                <el-radio-group v-model="infolist_filter.source_website_radio" class="cu_infolist_radio">
                    <el-radio :label="1">全部</el-radio>
                    <el-radio :label="2">贴吧</el-radio>
                    <el-radio :label="3">定向信源</el-radio>
                </el-radio-group>
                <el-tooltip class="item" effect="dark" content="点击跳转至定向监测" placement="top">
                    <i class="el-icon-edit custom-helper-info" @click="goto_dingxiangjiance"></i>
                </el-tooltip>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
            </el-col>
            <el-col :span="12">
                <div v-show="qitashijian">
                    <div style="font-size: 14px;line-height:19px;display: inline-block">其他时间：</div>
                    <div class="block zidingyi_date" style="display: inline-block;margin-left: 18px">
                        <el-date-picker
                                v-model="infolist_filter.time_value"
                                type="datetimerange"
                                range-separator="至"
                                start-placeholder="开始日期"
                                end-placeholder="结束日期" size="mini">
                        </el-date-picker>
                    </div>
                    <hr style="background-color:#d2d5db;height: 1px;border: none;margin-top: 4px"/>
                </div>
                <div v-show="kongbai">
                    <div style="font-size: 14px;line-height:19px;">&nbsp;</div>
                    <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                </div>
                <div style="font-size: 14px; display: inline-block">敏感属性：</div>
                <el-radio-group v-model="infolist_filter.sensitive_attr_radio" class="cu_infolist_radio">
                    <el-radio :label="1">全部</el-radio>
                    <el-radio :label="2">非敏感</el-radio>
                    <el-radio :label="3">敏感</el-radio>
                </el-radio-group>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                <div style="font-size: 14px; display: inline-block">相似文章：</div>
                <el-radio-group v-model="infolist_filter.similar_article_radio" class="cu_infolist_radio">
                    <el-radio :label="1">不合并</el-radio>
                    <el-radio :label="2">合并</el-radio>
                </el-radio-group>
                <el-tooltip class="item" effect="dark" content="提供时间跨度为35天以内的信息合并" placement="right">
                    <i class="el-icon-question custom-helper-info"></i>
                </el-tooltip>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                <div style="font-size: 14px; display: inline-block">涉及方式：</div>
                <el-radio-group v-model="infolist_filter.related_method_radio" class="cu_infolist_radio">
                    <el-radio :label="1">全部</el-radio>
                    <el-radio :label="2">内容涉及</el-radio>
                    <el-radio :label="3">定位涉及</el-radio>
                </el-radio-group>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                <div style="font-size: 14px; display: inline-block">匹配方式：</div>
                <el-radio-group v-model="infolist_filter.match_method_radio" class="cu_infolist_radio">
                    <el-radio :label="1">按全文</el-radio>
                    <el-radio :label="2">按标题</el-radio>
                    <el-radio :label="3">按正文</el-radio>
                </el-radio-group>
                <br/>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                <div style="font-size: 14px;line-height:19px;">&nbsp;</div>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
                <div style="font-size: 14px;line-height:19px;">&nbsp;</div>
                <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
            </el-col>
        </el-row>
        <el-row style="padding-left: 10px;margin-bottom: 0px">
            <div style="font-size: 14px; display: inline-block;">来源类型（多选）：</div>
            <el-checkbox class="laiyuanleixing"
                         :indeterminate="infolist_filter.isIndeterminate"
                         v-model="infolist_filter.domain_checkAll"
                         @change="source_type_handleCheckAllChange">全选
            </el-checkbox>
            <el-checkbox-group v-model="infolist_filter.source_type_checkList" class="laiyuanleixing"
                               @change="search_source" style="margin-left: 10px">
                <el-checkbox label="微博">微博</el-checkbox>
                <!--<el-checkbox label="2">网站</el-checkbox>-->
                <el-checkbox label="微信">微信</el-checkbox>
                <el-checkbox label="论坛">论坛</el-checkbox>
                <!--<el-checkbox label="客户端"></el-checkbox>-->
                <el-checkbox label="新闻">新闻</el-checkbox>
                <!--<el-checkbox label="博客"></el-checkbox>-->
                <!--<el-checkbox label="报刊"></el-checkbox>-->
                <!--<el-checkbox label="外媒"></el-checkbox>-->
            </el-checkbox-group>
            <el-tooltip class="item" effect="dark" content="新闻类型是具有新闻类备案号，或宣传部主办的网站，大型网站的新闻版块"
                        placement="right">
                <i class="el-icon-question custom-helper-info"></i>
            </el-tooltip>

            <hr style="background-color:#d2d5db;height: 1px;border: none;"/>
        </el-row>
        <div style="text-align:center">
            <el-button @click="filterData"
                       style="color: white;margin-right: 10px;width: 150px;background-color: #32a314"
                       size="small">查询
            </el-button>
            <el-button
                    style="box-shadow: 1px 1px 1px rgb(205,208,214);margin-right: 10px;width: 150px;background-color: rgb(232,235,241);color: #67C23A;border-color: transparent"
                    size="small">保存
            </el-button>
        </div>
    </div>

</template>

<script>
    const source_type = ['微博', '微信', '论坛', '新闻'];
    export default {
        name: "yq-main-infolist-top",
        data() {
            return {
                infolist_filter: {
                    time_range_radio: 1,
                    article_order_radio: 1,
                    result_show_radio: 1,
                    repost_weibo_radio: 1,
                    msg_region: '四川',
                    msg_region_radio: 2,
                    weibo_content_radio: 1,
                    source_website_radio: 1,
                    sensitive_attr_radio: 1,
                    similar_article_radio: 1,
                    related_method_radio: 1,
                    match_method_radio: 1,
                    source_type_checkList: ['微信'],
                    source_type_checkAll: false,
                    isIndeterminate: true,
                    time_value: '',

                },

                options: [{
                    value: '选项1',
                    label: '全部'
                }, {
                    value: '选项2',
                    label: '山西'
                }, {
                    value: '选项3',
                    label: '上海'
                }, {
                    value: '选项4',
                    label: '北京'
                }, {
                    value: '选项5',
                    label: '重庆'
                }, {
                    value: '选项6',
                    label: '四川'
                }],

                kongbai: true,
                qitashijian: false,
            }
        },
        methods: {

            filterData() {
                this.$emit("emitFilterData", this.infolist_filter)
            },
            source_type_handleCheckAllChange(val) {
                this.infolist_filter.source_type_checkList = val ? source_type : [];
                console.log("source_type_checkList",this.infolist_filter.source_type_checkList)
                this.infolist_filter.isIndeterminate = false
            },
            zidingyishijian() {
                if (this.infolist_filter.time_range_radio === 7) {
                    this.qitashijian = true;
                    this.kongbai = false
                } else {
                    this.qitashijian = false;
                    this.kongbai = true
                }
            },
            xinyuanquyu() {
                if (this.value !== '') {
                    this.infolist_filter.msg_region_radio = 1
                }
            },
            xinyuanquyu_danxuan() {
                if (this.infolist_filter.msg_region_radio === 2 | 3) {
                    this.value = ''
                }
            },
            goto_dingxiangjiance() {
                this.activeName = 'fifth'
            },
            search_source(selected) {
                this.infolist_filter.source_type_checkList=selected
                console.log('source_type_checkList',this.infolist_filter.source_type_checkList)
            },
        },
    }
</script>

<style lang="scss">
    .laiyuanleixing {
        .el-checkbox.is-bordered {
            padding: 5px 5px 5px 5px;
            line-height: normal;
        }
        .el-checkbox.is-bordered.is-checked {
            padding: 5px 5px 5px 5px;
            line-height: normal;
        }
        .el-checkbox__input.is-checked .el-checkbox__inner, .el-checkbox__input.is-indeterminate .el-checkbox__inner {
            background-color: orange;
            border-color: orange;
        }
        .el-checkbox__input.is-checked + .el-checkbox__label {
            color: orange;
        }
    }

    .cu_infolist_radio {
        .el-radio__input {
            display: none !important;
        }

        .el-radio {
            color: #81848a !important;
            padding-left: 0px !important;
            margin-left: 10px !important;
        }

        .el-radio__input.is-checked + .el-radio__label {
            color: orange;
            font-weight: 700;
        }
    }
</style>