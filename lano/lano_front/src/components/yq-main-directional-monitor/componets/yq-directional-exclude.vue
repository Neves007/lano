<template>
    <div>
        <el-row class="cu_domain_row">
            <el-select v-model="directional_data.ex_directional_add_method"
                       placeholder="请选择"
                       style="margin-top: 20px;margin-left: 20px"
                       @change="ex_dir_inputChange">
                <el-option
                        v-for="item in directional_data.options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
            <el-button type="text" icon="el-icon-location"
                       @click="directional_data.ex_mutipleAdd_dialogVisible = true"
                       v-if="directional_data.ex_showMutipleAddBtn">通过省份选择网站
            </el-button>
            <el-dialog class="cu_dir_dialog" title="选择要加入监测的网站"
                       :visible.sync="directional_data.ex_mutipleAdd_dialogVisible"
                       width="50%" :before-close="handleClose">
                <span>请选择要排除网站，支持多选，最多不能超出300个！</span>
                <el-transfer class="cu_transfer_btn"
                             filterable
                             :filter-method="filterMethod"
                             filter-placeholder="输入网站名称查询"
                             v-model="directional_data.ex_value2"
                             :titles="['所有监测网站','定向排除网站']"
                             :button-texts="['删除', '增加']"
                             :data="directional_data.ex_data2"
                             style="margin-top: 10px">
                </el-transfer>
                <span slot="footer" class="dialog-footer">
                                                <el-button class="cu_dialogBtn" type="primary"
                                                           @click="directional_data.ex_mutipleAdd_dialogVisible = false">保存</el-button>
                                                <el-button class="cu_dialogBtn"
                                                           @click="directional_data.ex_mutipleAdd_dialogVisible = false">关闭</el-button>
                                            </span>
            </el-dialog>

            <el-input class="cu_directional_input"
                      v-model="directional_data.ex_websiteInput"
                      v-if="directional_data.ex_showWebsiteInput"
                      placeholder="请输入网站域名，例如www.sina.com"></el-input>
            <el-input class="cu_directional_input" v-model="directional_data.ex_weiboInput"
                      v-if="directional_data.ex_showWeiboInput"
                      placeholder="请输入微博昵称，例如：央视新闻"></el-input>
            <el-input class="cu_directional_input" v-model="directional_data.ex_wechatInput"
                      v-if="directional_data.ex_showWechatInput"
                      placeholder="请输入微信公众号或微信号，例如：三剑客"></el-input>
            <el-input class="cu_directional_input" v-model="directional_data.ex_tiebaInput"
                      v-if="directional_data.ex_showTiebaInput"
                      placeholder="请输入贴吧昵称，例如：李毅吧"></el-input>

            <el-button v-if="directional_data.ex_showbtn"
                       style="margin-left: 10px;background-color: orange;color: white;">添加
            </el-button>
            <el-button v-if="directional_data.ex_showbtn"
                       style="margin-left: 0;background-color: #bbbbbb;color: white;">清空
            </el-button>

        </el-row>
        <el-tabs v-model="directional_data.ex_tabName" class="cu_directional_tab"
                 :tab-position="directional_data.tabPosition"
                 type="border-card" @tab-click="ex_dirTab_showInput">
            <el-tab-pane label="网站域名" name="0">
                <el-table
                        :data="directional_data.dir_website_tableData"
                        border
                        style="width: 100%">
                    <el-table-column
                            prop="name"
                            label="网站名称"
                            width="300">
                    </el-table-column>
                    <el-table-column
                            prop="domain"
                            label="域名"
                            width="780">
                    </el-table-column>
                    <el-table-column
                            prop="status"
                            label="状态"
                            width="100">
                        <template slot-scope="scope">
                            <el-tag type="success">成功</el-tag>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="operation"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button @click="handleClick(scope.row)" size="small"
                                       style="background-color: red;color: white ">取消监测
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
            <el-tab-pane label="微博昵称" name="1">
                <el-table
                        :data="directional_data.dir_weibo_tableData"
                        border
                        style="width: 100%">
                    <el-table-column
                            prop="name"
                            label="昵称"
                            width="300">
                    </el-table-column>
                    <el-table-column
                            prop="uid"
                            label="微博ID"
                            width="780">
                    </el-table-column>
                    <el-table-column
                            prop="status"
                            label="状态"
                            width="100">
                        <template slot-scope="scope">
                            <el-tag type="success">成功</el-tag>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="operation"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button @click="handleClick(scope.row)" size="small"
                                       style="background-color: red;color: white ">取消监测
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
            <el-tab-pane label="微信公众号" name="2">
                <el-table
                        :data="directional_data.dir_wechat_tableData"
                        border
                        style="width: 100%">
                    <el-table-column
                            prop="name"
                            label="公众号名称"
                            width="300">
                    </el-table-column>
                    <el-table-column
                            prop="wxid"
                            label="微信号"
                            width="780">
                    </el-table-column>
                    <el-table-column
                            prop="status"
                            label="状态"
                            width="100">
                        <template slot-scope="scope">
                            <el-tag type="success">成功</el-tag>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="operation"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button
                                    size="small"
                                    style="background-color: red;color: white ">取消监测
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
            <el-tab-pane label="贴吧昵称" name="3">
                <el-table
                        :data="directional_data.dir_tieba_tableData"
                        border
                        style="width: 100%">
                    <el-table-column
                            prop="name"
                            label="吧名"
                            width="300">
                    </el-table-column>
                    <el-table-column
                            prop="introduction"
                            label="贴吧介绍"
                            width="780">
                    </el-table-column>
                    <el-table-column
                            prop="status"
                            label="状态"
                            width="100">
                        <template slot-scope="scope">
                            <el-tag type="success">成功</el-tag>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="operation"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button @click="handleClick(scope.row)" size="small"
                                       style="background-color: red;color: white ">取消监测
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
    export default {
        name: "yq-directional-exclude",
        data() {
            const dir_generateData2 = _ => {
                const data = []
                const cities = ['上海', '北京', '广州', '深圳', '南京', '西安', '成都']
                const pinyin = ['shanghai', 'beijing', 'guangzhou', 'shenzhen', 'nanjing', 'xian', 'chengdu']
                cities.forEach((city, index) => {
                    data.push({
                        label: city,
                        key: index,
                        pinyin: pinyin[index]
                    })
                })
                return data
            }
            return{
                directional_data: {
                    ex_directional_add_method: '选项1',
                    options: [{
                        value: '选项1',
                        label: '单条添加'
                    }, {
                        value: '选项2',
                        label: '按省份批量添加网站'
                    }],
                    ex_mutipleAdd_dialogVisible: false,
                    ex_showMutipleAddBtn: false,
                    ex_value2: [],
                    ex_data2: dir_generateData2(),
                    ex_websiteInput: '',
                    ex_weiboInput: '',
                    ex_wechatInput: '',
                    ex_tiebaInput: '',
                    ex_showWebsiteInput: true,
                    ex_showWeiboInput: false,
                    ex_showWechatInput: false,
                    ex_showTiebaInput: false,
                    ex_showbtn: true,
                    ex_tabName: '0',
                    tabPosition: 'left',
                    dir_website_tableData: [],
                    dir_weibo_tableData: [],
                    dir_wechat_tableData: [],
                    dir_tieba_tableData: [],

                    myChart1: null,
                    myChart2: null,


                }

            }
        },
        methods:{
            ex_dir_inputChange() {
                if (this.directional_data.ex_directional_add_method === '选项2') {
                    this.directional_data.ex_showMutipleAddBtn = true
                    this.directional_data.ex_showWebsiteInput = false
                    this.directional_data.ex_showWeiboInput = false
                    this.directional_data.ex_showWechatInput = false
                    this.directional_data.ex_showTiebaInput = false
                    this.directional_data.ex_showbtn = false
                }
                if (this.directional_data.ex_directional_add_method === '选项1') {
                    switch (this.directional_data.ex_tabName) {
                        case '0':
                            this.directional_data.ex_showMutipleAddBtn = false
                            this.directional_data.ex_showWebsiteInput = true
                            this.directional_data.ex_showWeiboInput = false
                            this.directional_data.ex_showWechatInput = false
                            this.directional_data.ex_showTiebaInput = false
                            break

                        case '1':
                            this.directional_data.ex_showMutipleAddBtn = false
                            this.directional_data.ex_showWebsiteInput = false
                            this.directional_data.ex_showWeiboInput = true
                            this.directional_data.ex_showWechatInput = false
                            this.directional_data.ex_showTiebaInput = false
                            break

                        case '2':
                            this.directional_data.ex_showMutipleAddBtn = false
                            this.directional_data.ex_showWebsiteInput = false
                            this.directional_data.ex_showWeiboInput = false
                            this.directional_data.ex_showWechatInput = true
                            this.directional_data.ex_showTiebaInput = false
                            break

                        case '3':
                            this.directional_data.ex_showMutipleAddBtn = false
                            this.directional_data.ex_showWebsiteInput = false
                            this.directional_data.ex_showWeiboInput = false
                            this.directional_data.ex_showWechatInput = false
                            this.directional_data.ex_showTiebaInput = true
                            break
                    }
                    this.directional_data.ex_showbtn = true
                }
            },
            ex_dirTab_showInput() {
                let val = event.target.getAttribute('id')
                if (val === 'tab-0') {
                    if (this.directional_data.ex_directional_add_method === '选项1') {
                        this.directional_data.ex_showMutipleAddBtn = false
                        this.directional_data.ex_showWebsiteInput = true
                        this.directional_data.ex_showWeiboInput = false
                        this.directional_data.ex_showWechatInput = false
                        this.directional_data.ex_showTiebaInput = false
                        this.directional_data.ex_showbtn = true
                    }
                    if (this.directional_data.ex_directional_add_method === '选项2') {
                        this.directional_data.ex_showMutipleAddBtn = true
                        this.directional_data.ex_showWebsiteInput = false
                        this.directional_data.ex_showWeiboInput = false
                        this.directional_data.ex_showWechatInput = false
                        this.directional_data.ex_showTiebaInput = false
                        this.directional_data.ex_showbtn = false
                    }
                }
                if (val === 'tab-1') {
                    if (this.directional_data.ex_directional_add_method === '选项1') {
                        this.directional_data.ex_showMutipleAddBtn = false
                        this.directional_data.ex_showWebsiteInput = false
                        this.directional_data.ex_showWeiboInput = true
                        this.directional_data.ex_showWechatInput = false
                        this.directional_data.ex_showTiebaInput = false
                        this.directional_data.ex_showbtn = true
                    }
                    if (this.directional_data.ex_directional_add_method === '选项2') {
                        this.directional_data.ex_showMutipleAddBtn = true
                        this.directional_data.ex_showWebsiteInput = false
                        this.directional_data.ex_showWeiboInput = false
                        this.directional_data.ex_showWechatInput = false
                        this.directional_data.ex_showTiebaInput = false
                        this.directional_data.ex_showbtn = false
                    }
                }
                if (val === 'tab-2') {
                    if (this.directional_data.ex_directional_add_method === '选项1') {
                        this.directional_data.ex_showMutipleAddBtn = false
                        this.directional_data.ex_showWebsiteInput = false
                        this.directional_data.ex_showWeiboInput = false
                        this.directional_data.ex_showWechatInput = true
                        this.directional_data.ex_showTiebaInput = false
                        this.directional_data.ex_showbtn = true
                    }
                    if (this.directional_data.ex_directional_add_method === '选项2') {
                        this.directional_data.ex_showMutipleAddBtn = true
                        this.directional_data.ex_showWebsiteInput = false
                        this.directional_data.ex_showWeiboInput = false
                        this.directional_data.ex_showWechatInput = false
                        this.directional_data.ex_showTiebaInput = false
                        this.directional_data.ex_showbtn = false
                    }
                }
                if (val === 'tab-3') {
                    if (this.directional_data.ex_directional_add_method === '选项1') {
                        this.directional_data.ex_showMutipleAddBtn = false
                        this.directional_data.ex_showWebsiteInput = false
                        this.directional_data.ex_showWeiboInput = false
                        this.directional_data.ex_showWechatInput = false
                        this.directional_data.ex_showTiebaInput = true
                        this.directional_data.ex_showbtn = true
                    }
                    if (this.directional_data.ex_directional_add_method === '选项2') {
                        this.directional_data.ex_showMutipleAddBtn = true
                        this.directional_data.ex_showWebsiteInput = false
                        this.directional_data.ex_showWeiboInput = false
                        this.directional_data.ex_showWechatInput = false
                        this.directional_data.ex_showTiebaInput = false
                        this.directional_data.ex_showbtn = false
                    }
                }
            },
            handleClick(tab, event) {
                this.initGraph()
                if (tab._props['name'] === 'collapse') {
                    this.mainContentSpan = 24
                    this.asideSpan = 0
                } else {
                    this.mainContentSpan = 20
                    this.asideSpan = 4
                }
                this.$nextTick(function () {
                    this.myChart1.resize()
                    this.myChart2.resize()
                    for (let i in this.$refs) {
                        if (this.$refs[i].hasOwnProperty('echarts')) {
                            this.$refs[i].echarts.resize()
                        }
                    }
                })
            },

        }
    }
</script>

<style scoped>

</style>