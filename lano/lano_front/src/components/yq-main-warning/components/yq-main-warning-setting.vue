<template>
    <el-form ref="form" :model="form_warning" :rules="rules"
             label-position="left" label-width="150px">
        <div v-if="show_setting">
            <el-row class="warning_row">
                <div class="warning_header">
                    <div style="border-left: 4px solid orange;margin-top: 5px;display: inline-block;text-align: center">
                        <span style="margin-left: 20px;font-size: small"><b>预警词</b></span>
                    </div>
                </div>
                <el-row>
                    <div style="margin-left:20px; background-color:#ffe5b0; margin-right:20px; margin-top: 20px;height: 30px;">
                        <i style="margin-left: 8px" class="fa fa-lightbulb-o"></i>
                        <span style="margin-left:10px;background-color:#ffe5b0;  margin-top: 20px;height: 100%; width: 100%; font-size: small;line-height: 31px">
                                        预警词：基于您设置的监测方案，如果监测方案中涉及您以下设置的预警关键词，则给您推送预警信息，如果您不设置，那么系统会给您推送跟监测方案相关的信息</span>
                    </div>
                    <el-form-item label="设置预警词：" style="margin-top: 20px">
                        <el-input placeholder="请输入预警关键词" v-model="form_warning.word"
                                  style="width: 30%"></el-input>
                        <span>（可不填）</span>
                    </el-form-item>
                </el-row>
            </el-row>
            <el-row class="warning_row">
                <div class="warning_header">
                    <div style="border-left: 4px solid orange;margin-top: 5px; display: inline-block;text-align: center">
                        <span style="margin-left: 20px;font-size: small"><b>预警条件设置</b></span>
                    </div>
                </div>
                <el-row>
                    <el-form-item label="预警内容：" style="margin-left: 100px;margin-top: 20px">
                        <el-radio class="warning_radio" v-model="form_warning.content_radio"
                                  label="1"
                                  size="small" border
                                  style="margin-left: 10px;">全部
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.content_radio"
                                  label="2"
                                  size="small" border>敏感
                        </el-radio>
                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="来源类型：" style="margin-left: 100px;">
                        <el-checkbox-group class="warning_checkbox"
                                           v-model="form_warning.source_type_checkbox" size="small">
                            <el-checkbox label="全部" border></el-checkbox>
                            <el-checkbox label="微博" border></el-checkbox>
                            <!--<el-checkbox label="网站" border></el-checkbox>-->
                            <el-checkbox label="新闻" border></el-checkbox>
                            <el-checkbox label="微信" border></el-checkbox>
                            <!--<el-checkbox label="政务" border></el-checkbox>-->
                            <!--<el-checkbox label="视频" border></el-checkbox>-->
                            <!--<el-checkbox label="报刊" border></el-checkbox>-->
                            <el-checkbox label="论坛" border></el-checkbox>
                            <!--<el-checkbox label="客户端" border></el-checkbox>-->
                            <!--<el-checkbox label="博客" border></el-checkbox>-->
                            <!--<el-checkbox label="外媒" border></el-checkbox>-->
                        </el-checkbox-group>
                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="相似文章：" style="margin-left: 100px;">
                        <el-radio class="warning_radio" v-model="form_warning.similar_article_radio"
                                  label="1" size="small" border
                                  style="margin-left: 10px;">合并
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.similar_article_radio"
                                  label="2" size="small" border>不合并
                        </el-radio>
                    </el-form-item>
                </el-row>

                <el-row>
                    <el-form-item label="信源区域：" style="margin-left: 100px;">
                        <el-select class="warning_selector" v-model="form_warning.info_region"
                                   placeholder="全部" size="mini"
                                   style="margin-left: 10px;">
                            <el-option
                                    v-for="item in region_options"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                        <el-radio class="warning_radio" v-model="form_warning.region_radio"
                                  label="1"
                                  size="small" border
                                  style="margin-left: 10px;">省内
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.region_radio"
                                  label="2"
                                  size="small" border>省外
                        </el-radio>

                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="来源网站：" style="margin-left: 100px;">
                        <el-radio class="warning_radio" v-model="form_warning.source_website_radio"
                                  label="1" size="small" border
                                  style="margin-left: 10px;">全部
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.source_website_radio"
                                  label="2" size="small" border>贴吧
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.source_website_radio"
                                  label="3" size="small" border>定向信源
                        </el-radio>

                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="结果呈现：" style="margin-left: 100px;">
                        <el-radio class="warning_radio" v-model="form_warning.result_show_radio"
                                  label="1"
                                  size="small" border
                                  style="margin-left: 10px;">正常信息
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.result_show_radio"
                                  label="2"
                                  size="small" border>精准信息
                        </el-radio>
                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="转发微博：" style="margin-left: 100px;">
                        <el-radio class="warning_radio" v-model="form_warning.weibo_radio" label="1"
                                  size="small" border
                                  style="margin-left: 10px;">显示
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.weibo_radio" label="2"
                                  size="small" border>不显示
                        </el-radio>
                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="涉及方式：" style="margin-left: 100px;">
                        <el-radio class="warning_radio" v-model="form_warning.relate_method_radio"
                                  label="1"
                                  size="small" border
                                  style="margin-left: 10px;">全部
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.relate_method_radio"
                                  label="2"
                                  size="small" border>内容涉及
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.relate_method_radio"
                                  label="3"
                                  size="small" border>定位涉及
                        </el-radio>

                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="匹配方式：" style="margin-left: 100px;">
                        <el-radio class="warning_radio" v-model="form_warning.match_method_radio"
                                  label="1"
                                  size="small" border
                                  style="margin-left: 10px;">按全文
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.match_method_radio"
                                  label="2"
                                  size="small" border>按标题
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.match_method_radio"
                                  label="3"
                                  size="small" border>按正文
                        </el-radio>

                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="预警去重：" style="margin-left: 100px;">
                        <el-radio class="warning_radio"
                                  v-model="form_warning.remove_duplicate_radio"
                                  label="1" size="small" border
                                  style="margin-left: 10px;">开启
                        </el-radio>
                        <el-radio class="warning_radio"
                                  v-model="form_warning.remove_duplicate_radio"
                                  label="2" size="small" border>关闭
                        </el-radio>

                    </el-form-item>
                </el-row>

            </el-row>
            <el-row class="warning_row">
                <div class="warning_header">
                    <div style="border-left: 4px solid orange;margin-top: 5px;display: inline-block;text-align: center">
                        <span style="margin-left: 20px;font-size: small"><b>预警方式设置</b></span>
                    </div>
                </div>
                <el-row>
                    <el-form-item label="预警方式：" style="margin-left: 100px;margin-top: 20px">
                        <el-checkbox-group class="warning_checkbox"
                                           v-model="form_warning.warning_method_checkbox">
                            <el-tooltip class="item" effect="dark" content="邮件预警"
                                        placement="top">
                                <el-checkbox label="email" class="cu_method_button" border>
                                    <i class="fa fa-envelope cu_icon"
                                       style="margin-left: 14px;margin-top: -6px;"></i>
                                </el-checkbox>
                            </el-tooltip>
                            <el-tooltip class="item" effect="dark" content="短信预警"
                                        placement="top">
                                <el-checkbox label="sms" class="cu_method_button" border>
                                    <i class="fa fa-mobile-phone cu_icon"
                                       style="margin-left: 22px;margin-top: -6px;"></i>
                                </el-checkbox>
                            </el-tooltip>
                            <el-tooltip class="item" effect="dark" content="微信预警"
                                        placement="top">
                                <el-checkbox label="wechat" class="cu_method_button" border>
                                    <i class="fa fa-weixin cu_icon"
                                       style="margin-left: 11px;margin-top: -6px;"></i>
                                </el-checkbox>
                            </el-tooltip>
                            <el-tooltip class="item" effect="dark" content="客户端推送"
                                        placement="top">
                                <el-checkbox label="app" class="cu_method_button" border>
                                    <i class="fa fa-android cu_icon"
                                       style="margin-left: 17px;margin-top: -6px;"></i>
                                </el-checkbox>
                            </el-tooltip>
                            <el-tooltip class="item" effect="dark" content="PC弹窗预警"
                                        placement="top">
                                <el-checkbox label="pc" class="cu_method_button" border>
                                    <i class="fa fa-television cu_icon"
                                       style="margin-left: 11px;margin-top: -6px;"></i>
                                </el-checkbox>
                            </el-tooltip>
                        </el-checkbox-group>
                    </el-form-item>
                </el-row>
            </el-row>
            <el-row class="warning_row">
                <div class="warning_header">
                    <div style="border-left: 4px solid orange;margin-top: 5px;display: inline-block;text-align: center">
                        <span style="margin-left: 20px;font-size: small"><b>预警时间设置</b></span>
                    </div>
                </div>
                <el-row>
                    <el-form-item label="接收时间：" style="margin-left: 100px;margin-top: 20px">
                        <el-time-select class="cu_warning_time" arrow-control="true"
                                        v-model="form_warning.start_time"
                                        :picker-options="{
                                                start: '00:00',
                                                step: '01:00',
                                                end: '23:00'
                                                }"
                                        placeholder="08:00" style="margin-left: 10px;">
                        </el-time-select>
                        --
                        <el-time-select class="cu_warning_time" arrow-control="true"
                                        v-model="form_warning.end_time"
                                        :picker-options="{
                                                start: '00:00',
                                                step: '01:00',
                                                end: '23:00'
                                                }"
                                        placeholder="23:00">
                        </el-time-select>

                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="预警间隔：" style="margin-left: 100px;">
                        <el-radio class="warning_radio"
                                  v-model="form_warning.warning_interval_radio"
                                  label="1" size="small" border
                                  style="margin-left: 10px;">定时预警
                        </el-radio>
                        <el-radio class="warning_radio"
                                  v-model="form_warning.warning_interval_radio"
                                  label="2" size="small" border>实时预警
                        </el-radio>

                    </el-form-item>
                </el-row>
                <el-row>
                    <el-form-item label="周末预警：" style="margin-left: 100px;">
                        <el-radio class="warning_radio" v-model="form_warning.weekend_radio"
                                  label="1" size="small" border
                                  style="margin-left: 10px;">周末预警
                        </el-radio>
                        <el-radio class="warning_radio" v-model="form_warning.weekend_radio"
                                  label="2" size="small" border>周末不预警
                        </el-radio>

                    </el-form-item>
                </el-row>
            </el-row>
            <el-row>
                <el-form-item>
                    <el-button class="save" @click="saveWarning">保存</el-button>
                    <!--<el-button id="cancel">取消</el-button>-->
                </el-form-item>
            </el-row>
        </div>

    </el-form>
</template>

<script>
    import axios from 'axios'

    let base_url = 'http://127.0.0.1:8000/';
    export default {
        name: "yq-main-warning-setting",
        props: ['show_setting', 'currentPlan'],
        data() {
            return {
                warning_setting: {},
                form_warning: {
                    word: '',
                    content_radio: '1',
                    source_type_checkbox: [],
                    similar_article_radio: '1',
                    region_radio: '1',
                    source_website_radio: '1',
                    result_show_radio: '1',
                    info_region: '',
                    weibo_radio: '1',
                    relate_method_radio: '1',
                    match_method_radio: '1',
                    remove_duplicate_radio: '1',
                    warning_method_checkbox: [],
                    start_time: '08:00',
                    end_time: '23:00',
                    warning_interval_radio: '2',
                    weekend_radio: '1',
                },
            }
        },
        methods: {
            AddWarningSetting() {
                axios.post(base_url + 'api/add_warning', JSON.stringify(this.warning_setting)).then(r => {
                    if (r.data.error_num === 0) {
                        console.log('warning message %o',r);
                        // this.getPlans(); //that.plans 拿到
                        this.$message.success("预警设置成功")
                    } else {
                        console.log('传递失败', r.data.msg)
                        this.$message.error("预警设置失败")
                    }
                })
            },

            saveWarning() {
                this.warning_setting['plan_id'] = this.currentPlan.pk;
                this.warning_setting['warning_word'] = this.form_warning.word;
                this.warning_setting['warning_content_type'] = this.form_warning.content_radio;
                this.warning_setting['warning_source_type'] = this.form_warning.source_type_checkbox;
                this.warning_setting['warning_similar_article'] = this.form_warning.similar_article_radio;
                this.warning_setting['warning_region'] = this.form_warning.info_region;
                this.warning_setting['warning_region_type'] = this.form_warning.region_radio;
                this.warning_setting['warning_source_website'] = this.form_warning.source_website_radio;
                this.warning_setting['warning_result_show'] = this.form_warning.result_show_radio;
                this.warning_setting['warning_forward_weibo'] = this.form_warning.weibo_radio;
                this.warning_setting['warning_relate_method'] = this.form_warning.relate_method_radio;
                this.warning_setting['warning_match_method'] = this.form_warning.match_method_radio;
                this.warning_setting['warning_duplicate'] = this.form_warning.remove_duplicate_radio;
                this.warning_setting['warning_method_type'] = this.form_warning.warning_method_checkbox;
                this.warning_setting['warning_start_time'] = this.form_warning.start_time;
                this.warning_setting['warning_end_time'] = this.form_warning.end_time;
                this.warning_setting['warning_interval'] = this.form_warning.warning_interval_radio;
                this.warning_setting['warning_weekend'] = this.form_warning.weekend_radio;

                this.AddWarningSetting();
                // this.advance_form.name=''
                // this.advance_form.match=''
                // this.advance_form.except2=''
            },
        }

    }

</script>

<style scoped>

</style>