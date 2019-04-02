<template>
    <div>
        <el-row class="cu_domain_row">
            <el-select v-model="directional_data.directional_add_method" placeholder="请选择"
                       style="margin-top: 20px;margin-left: 20px" @change="dir_inputChange">
                <el-option
                        v-for="item in directional_data.options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
            <el-button type="text" icon="el-icon-location"
                       @click="directional_data.mutipleAdd_dialogVisible = true"
                       v-if="directional_data.showMutipleAddBtn">通过省份选择网站
            </el-button>
            <el-dialog class="cu_dir_dialog" title="选择要加入监测的网站"
                       :visible.sync="directional_data.mutipleAdd_dialogVisible" width="50%"
                       :before-close="handleClose">
                <span>请选择监测网站，支持多选，最多不能超出300个！</span>
                <el-transfer class="cu_transfer_btn"
                             filterable
                             :filter-method="filterMethod"
                             filter-placeholder="输入网站名称查询"
                             v-model="directional_data.value2"
                             :titles="['所有监测网站','定向监测网站']"
                             :button-texts="['删除', '增加']"
                             :data="directional_data.data2"
                             style="margin-top: 10px">
                </el-transfer>
                <span slot="footer" class="dialog-footer">
                    <el-button class="cu_dialogBtn" type="primary"
                               @click="directional_data.mutipleAdd_dialogVisible = false">保存</el-button>
                    <el-button class="cu_dialogBtn"
                               @click="directional_data.mutipleAdd_dialogVisible = false">关闭</el-button>
                </span>
            </el-dialog>

            <el-input class="cu_directional_input" v-model="directional_data.websiteInput"
                      v-if="directional_data.showWebsiteInput"
                      placeholder="请输入网站域名，例如www.sina.com" clearable="true"></el-input>
            <el-input class="cu_directional_input" v-model="directional_data.weiboInput"
                      v-if="directional_data.showWeiboInput"
                      placeholder="请输入微博昵称，例如：央视新闻" clearable="true"></el-input>
            <el-input class="cu_directional_input" v-model="directional_data.wechatInput"
                      v-if="directional_data.showWechatInput"
                      placeholder="请输入微信公众号或微信号，例如：三剑客" clearable="true"></el-input>
            <el-input class="cu_directional_input" v-model="directional_data.tiebaInput"
                      v-if="directional_data.showTiebaInput"
                      placeholder="请输入贴吧昵称，例如：李毅吧" clearable="true"></el-input>

            <el-button v-if="directional_data.showbtn" @click='addDir'
                       style="margin-left: 10px;background-color: orange;color: white;">添加
            </el-button>
            <!--<el-button v-if="directional_data.showbtn"-->
            <!--style="margin-left: 0;background-color: #bbbbbb;color: white;">清空-->
            <!--</el-button>-->

        </el-row>
        <el-tabs v-model="directional_data.tabName" class="cu_directional_tab"
                 :tab-position="directional_data.tabPosition"
                 type="border-card" @tab-click="dirTab_showInput">
            <el-tab-pane label="网站域名" name="0">
                <el-table
                        :data="directional_data.dir_website_tableData"
                        border
                        max-height="250"
                        style="width: 100%">
                    <el-table-column
                            prop="fields.name"
                            label="网站名称"
                            width="300">
                    </el-table-column>
                    <el-table-column
                            prop="fields.domain"
                            label="域名"
                            width="780">
                    </el-table-column>
                    <el-table-column
                            prop="fields.status"
                            label="状态"
                            width="100">
                        <template slot-scope="scope">
                            <el-tag type="success" v-if="scope.row.fields.status">成功</el-tag>
                            <el-tag type="danger" v-else>失败</el-tag>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="operation"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button @click="deleteDomain(scope.row.pk)" size="small"
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
                        max-height="250"
                        style="width: 100%">
                    <el-table-column
                            prop="fields.name"
                            label="昵称"
                            width="300">
                    </el-table-column>
                    <el-table-column
                            prop="fields.uid"
                            label="微博ID"
                            width="780">
                    </el-table-column>

                    <el-table-column
                            prop="fields.status"
                            label="状态"
                            width="100">
                        <template slot-scope="scope">
                            <el-tag type="success" v-if="scope.row.fields.status">成功</el-tag>
                            <el-tag type="danger" v-else>失败</el-tag>
                        </template>
                    </el-table-column>

                    <el-table-column
                            prop="operation"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button @click="deleteWeibo(scope.row.pk)" size="small"
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
                        max-height="250"
                        style="width: 100%">
                    <el-table-column
                            prop="fields.name"
                            label="公众号名称"
                            width="300">
                    </el-table-column>
                    <el-table-column
                            prop="fields.wxid"
                            label="微信号"
                            width="780">
                    </el-table-column>
                    <el-table-column
                            prop="fields.status"
                            label="状态"
                            width="100">
                        <template slot-scope="scope">
                            <el-tag type="success" v-if="scope.row.fields.status">成功</el-tag>
                            <el-tag type="danger" v-else>失败</el-tag>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="operation"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button @click="deleteWechat(scope.row.pk)" size="small"
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
    import axios from 'axios'
    let base_url = 'http://127.0.0.1:8000/';


    export default {
        name: "yq-directional-monitor",
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
                    directional_add_method: '选项1',
                    options: [{
                        value: '选项1',
                        label: '单条添加'
                    }, {
                        value: '选项2',
                        label: '按省份批量添加网站'
                    }],
                    mutipleAdd_dialogVisible: false,
                    showMutipleAddBtn: false,
                    value2: [],
                    data2: dir_generateData2(),
                    websiteInput: '',
                    weiboInput: '',
                    wechatInput: '',
                    tiebaInput: '',
                    showWebsiteInput: true,
                    showWeiboInput: false,
                    showWechatInput: false,
                    showTiebaInput: false,
                    showbtn: true,
                    tabName: '0',
                    tabPosition: 'left',
                    dir_website_tableData: [],
                    dir_weibo_tableData: [],
                    dir_wechat_tableData: [],

                }

            }
        },
        props: ['currentPlan'],
        methods:{
            dir_inputChange() {
                if (this.directional_data.directional_add_method === '选项2') {
                    this.directional_data.showMutipleAddBtn = true
                    this.directional_data.showWebsiteInput = false
                    this.directional_data.showWeiboInput = false
                    this.directional_data.showWechatInput = false
                    this.directional_data.showTiebaInput = false
                    this.directional_data.showbtn = false
                }
                if (this.directional_data.directional_add_method === '选项1') {
                    switch (this.directional_data.tabName) {
                        case '0':
                            this.directional_data.showMutipleAddBtn = false
                            this.directional_data.showWebsiteInput = true
                            this.directional_data.showWeiboInput = false
                            this.directional_data.showWechatInput = false
                            this.directional_data.showTiebaInput = false
                            break

                        case '1':
                            this.directional_data.showMutipleAddBtn = false
                            this.directional_data.showWebsiteInput = false
                            this.directional_data.showWeiboInput = true
                            this.directional_data.showWechatInput = false
                            this.directional_data.showTiebaInput = false
                            break

                        case '2':
                            this.directional_data.showMutipleAddBtn = false
                            this.directional_data.showWebsiteInput = false
                            this.directional_data.showWeiboInput = false
                            this.directional_data.showWechatInput = true
                            this.directional_data.showTiebaInput = false
                            break

                        case '3':
                            this.directional_data.showMutipleAddBtn = false
                            this.directional_data.showWebsiteInput = false
                            this.directional_data.showWeiboInput = false
                            this.directional_data.showWechatInput = false
                            this.directional_data.showTiebaInput = true
                            break
                    }
                    this.directional_data.showbtn = true
                }
            },
            addDir() {
                if (this.directional_data.websiteInput.length !== 0) {
                    axios.post(base_url + 'api/monitor_web_add', {
                        // 'name': '这是一个网站名称',
                        'domain': this.directional_data.websiteInput,
                        'planid':this.currentPlan.pk
                    }).then(r => {
                        // console.log('response %o', r)
                        if (r.data.error_num === 0) {
                            this.getDomainList();
                        }
                        else {
                            console.log('保存失败',r.data.msg)
                            this.$message.error("该监测网站已存在")
                        }
                        this.directional_data.websiteInput = ''
                    }).catch(err => {
                        console.log('error %o', err)
                        this.$message.error("请输入正确域名")
                    })
                }
                if (this.directional_data.weiboInput.length !== 0) {
                    axios.post(base_url + 'api/monitor_weibo_add', {
                        'name': this.directional_data.weiboInput,
                        'planid':this.currentPlan.pk
                    }).then(r => {
                        // console.log('response %o', r)
                        if (r.data.error_num === 0) {
                            this.getWeiboList();
                        }
                        else {
                            console.log('保存失败',r.data.msg)
                            this.$message.error("该监测微博已存在")
                        }
                        this.directional_data.weiboInput = ''
                    }).catch(err => {
                        console.log('error %o', err)
                    })
                }
                if (this.directional_data.wechatInput.length !== 0) {
                    axios.post(base_url + 'api/monitor_wechat_add', {
                        'name': this.directional_data.wechatInput,
                        'planid':this.currentPlan.pk
                    }).then(r => {
                        // console.log('response %o', r)
                        if (r.data.error_num === 0) {
                            this.getWechatList();
                        }
                        else {
                            console.log('保存失败',r.data.msg)
                            this.$message.error("该监测公众号已存在")
                        }
                        this.directional_data.wechatInput = ''
                    }).catch(err => {
                        console.log('error %o', err)
                    })
                }
            },
            getDomainList() {
                let that = this
                axios.post(base_url + 'api/get_monitor_web', {'planid':this.currentPlan.pk}).then((r) => {
                    if (r.data.error_num === 0) {
                        // console.log('monitor_web %o',r)
                        that.directional_data.dir_website_tableData = r.data.list
                    }
                    // console.log('response %o', r)
                }).catch(err => {
                    console.log('error %o', err)
                })
            },
            deleteDomain(del_index) {
                // console.log(del_index)
                axios.post(base_url + 'api/monitor_web_delete',del_index).then(r => {
                    // console.log('response %o', r)
                    if (r.data.error_num === 0) {
                        this.getDomainList();
                    }
                }).catch(err => {
                    console.log('error %o', err)
                })
            },
            getWeiboList() {
                let that = this
                axios.post(base_url + 'api/get_monitor_weibo', {'planid':this.currentPlan.pk}).then((r) => {
                    if (r.data.error_num === 0) {
                        // console.log('monitor_web %o',r)
                        that.directional_data.dir_weibo_tableData = r.data.list
                    }
                    // console.log('response %o', r)
                }).catch(err => {
                    console.log('error %o', err)
                })
            },
            deleteWeibo(del_index) {
                axios.post(base_url + 'api/monitor_weibo_delete',del_index).then(r => {
                    console.log('response %o', r)
                    console.log('planid',this.currentPlan.pk)
                    if (r.data.error_num === 0) {
                        this.getWeiboList();
                    }
                }).catch(err => {
                    console.log('error %o', err)
                })
            },
            getWechatList() {
                let that = this
                axios.post(base_url + 'api/get_monitor_wechat', {'planid':this.currentPlan.pk}).then((r) => {
                    if (r.data.error_num === 0) {
                        // console.log('monitor_web %o',r)
                        that.directional_data.dir_wechat_tableData = r.data.list
                    }
                    // console.log('response %o', r)
                }).catch(err => {
                    console.log('error %o', err)
                })
            },
            deleteWechat(del_index) {
                axios.post(base_url + 'api/monitor_wechat_delete',del_index).then(r => {
                    console.log('response %o', r)
                    if (r.data.error_num === 0) {
                        this.getWechatList();
                    }
                }).catch(err => {
                    console.log('error %o', err)
                })
            },
            dirTab_showInput() {
                let val = event.target.getAttribute('id')
                if (val === 'tab-0') {
                    if (this.directional_data.directional_add_method === '选项1') {
                        this.directional_data.showMutipleAddBtn = false
                        this.directional_data.showWebsiteInput = true
                        this.directional_data.showWeiboInput = false
                        this.directional_data.showWechatInput = false
                        this.directional_data.showTiebaInput = false
                        this.directional_data.showbtn = true
                    }
                    if (this.directional_data.directional_add_method === '选项2') {
                        this.directional_data.showMutipleAddBtn = true
                        this.directional_data.showWebsiteInput = false
                        this.directional_data.showWeiboInput = false
                        this.directional_data.showWechatInput = false
                        this.directional_data.showTiebaInput = false
                        this.directional_data.showbtn = false
                    }
                }
                if (val === 'tab-1') {
                    if (this.directional_data.directional_add_method === '选项1') {
                        this.directional_data.showMutipleAddBtn = false
                        this.directional_data.showWebsiteInput = false
                        this.directional_data.showWeiboInput = true
                        this.directional_data.showWechatInput = false
                        this.directional_data.showTiebaInput = false
                        this.directional_data.showbtn = true
                    }
                    if (this.directional_data.directional_add_method === '选项2') {
                        this.directional_data.showMutipleAddBtn = true
                        this.directional_data.showWebsiteInput = false
                        this.directional_data.showWeiboInput = false
                        this.directional_data.showWechatInput = false
                        this.directional_data.showTiebaInput = false
                        this.directional_data.showbtn = false
                    }
                }
                if (val === 'tab-2') {
                    if (this.directional_data.directional_add_method === '选项1') {
                        this.directional_data.showMutipleAddBtn = false
                        this.directional_data.showWebsiteInput = false
                        this.directional_data.showWeiboInput = false
                        this.directional_data.showWechatInput = true
                        this.directional_data.showTiebaInput = false
                        this.directional_data.showbtn = true
                    }
                    if (this.directional_data.directional_add_method === '选项2') {
                        this.directional_data.showMutipleAddBtn = true
                        this.directional_data.showWebsiteInput = false
                        this.directional_data.showWeiboInput = false
                        this.directional_data.showWechatInput = false
                        this.directional_data.showTiebaInput = false
                        this.directional_data.showbtn = false
                    }
                }
                if (val === 'tab-3') {
                    if (this.directional_data.directional_add_method === '选项1') {
                        this.directional_data.showMutipleAddBtn = false
                        this.directional_data.showWebsiteInput = false
                        this.directional_data.showWeiboInput = false
                        this.directional_data.showWechatInput = false
                        this.directional_data.showTiebaInput = true
                        this.directional_data.showbtn = true
                    }
                    if (this.directional_data.directional_add_method === '选项2') {
                        this.directional_data.showMutipleAddBtn = true
                        this.directional_data.showWebsiteInput = false
                        this.directional_data.showWeiboInput = false
                        this.directional_data.showWechatInput = false
                        this.directional_data.showTiebaInput = false
                        this.directional_data.showbtn = false
                    }
                }
            },
        },
        mounted() {
            this.getDomainList();
            this.getWeiboList();
            this.getWechatList();

        }
    }
</script>

<style scoped>

</style>