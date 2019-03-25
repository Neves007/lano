<template>
    <tbody>
    <tr>
        <td>
            <div class="choose">
                <el-checkbox v-model="checked" @change="chooseAll"></el-checkbox>
            </div>
        </td>
        <td colspan="5">
            <div>
                <div style="float: left">
                    <span>批量操作：</span>
                    <el-tooltip class="item" effect="dark" content="加入收藏夹"
                                placement="bottom">
                        <el-button type="info" style="padding: 4px 4px; "
                                   @click="insert_shoucangjia">
                            <d2-icon-svg name="like"
                                         style="width: 14px; height: 13px;color: white;fill: white;align-items: center"/>
                        </el-button>
                    </el-tooltip>
                    <el-dialog
                            title="素材操作"
                            :visible.sync="piliang_jiarushoucangjia"
                            width="10%"
                            class="sucaicaozuo_dialog"
                            style="margin-top: 45vh;">
                        <span>您已选择{{news_number}}个新闻，确认要加入到收藏夹吗？</span>
                        <span slot="footer" class="dialog-footer">
                                                        <el-button type="success"
                                                                   style="box-shadow: 1px 1px 1px #376e00;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #32a314;
                                                                   text-align: center"
                                                                   size="mini"
                                                                   @click="piliang_jiarushoucangjia = false">确定
                                                        </el-button>
                                                        <el-button @click="piliang_jiarushoucangjia = false"
                                                                   style="box-shadow: 1px 1px 1px grey;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取消
                                                        </el-button>
                                </span>
                    </el-dialog>


                    <el-tooltip class="item" effect="dark" content="加入简报素材"
                                placement="bottom">
                        <el-button type="info" style="padding: 4px 4px;margin-left: 10px"
                                   @click="insert_jianbaosucai">
                            <d2-icon-svg name="tag"
                                         style="width: 14px; height: 13px;color: white;fill: white;"/>
                        </el-button>
                    </el-tooltip>
                    <el-dialog
                            title="素材操作"
                            :visible.sync="piliang_jiarujianbaosucai"
                            width="10%"
                            class="sucaicaozuo_dialog"
                            style="margin-top: 45vh;">
                        <span>您已选择{{news_number}}个新闻，确认要加入到素材库吗？</span>
                        <span slot="footer" class="dialog-footer">
                                                        <el-button type="success"
                                                                   style="box-shadow: 1px 1px 1px #376e00;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #32a314;
                                                                   text-align: center"
                                                                   size="mini"
                                                                   @click="piliang_jiarujianbaosucai = false">确定
                                                        </el-button>
                                                        <el-button @click="piliang_jiarujianbaosucai = false"
                                                                   style="box-shadow: 1px 1px 1px grey;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取 消
                                                        </el-button>
                                                    </span>
                    </el-dialog>

                    <el-dropdown style="margin-left: 10px;margin-right: 10px" size="mini">
                                                    <span class="el-dropdown-link">
                                                        <el-button type="info" style="padding: 4px 4px; ">
                                                            <d2-icon-svg name="share"
                                                                         style="width: 14px; height: 13px;color: white;fill: white;"/>
                                                            <i class="el-icon-arrow-down el-icon--right"
                                                               style="margin-left: 1px;font-size: 1px"></i>
                                                        </el-button>
                                                    </span>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item>
                                <el-tooltip class="item" effect="dark" content="短信发送舆情"
                                            placement="right">
                                    <i class="fa fa-mobile-phone"
                                       style="font-size: 30px"
                                       @click="duanxin_tongxunlu=true"></i>
                                </el-tooltip>
                            </el-dropdown-item>
                            <el-dropdown-item>
                                <el-tooltip class="item" effect="dark" content="邮件发送舆情"
                                            placement="right">
                                    <i class="fa fa-envelope"
                                       style="font-size: 15px"
                                       @click="youxiang_tongxunlu=true"></i>
                                </el-tooltip>
                            </el-dropdown-item>
                            <el-dropdown-item>
                                <el-tooltip class="item" effect="dark" content="微信分享舆情"
                                            placement="right">
                                    <i class="fa fa-weixin"
                                       style="font-size: 16px"
                                       @click="wechat_tongxunlu=true"></i>
                                </el-tooltip>
                            </el-dropdown-item>
                            <el-dropdown-item>
                                <el-tooltip class="item" effect="dark" content="QQ分享舆情"
                                            placement="right">
                                    <i class="fa fa-qq" style="font-size: 16px"></i>
                                </el-tooltip>
                            </el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                    <el-dialog
                            title="联系人来自通讯录"
                            :visible.sync="duanxin_tongxunlu"
                            width="60%"
                            class="tongxunlu_dialog"
                    >
                        <el-table :data="tongxunluData">
                            <el-table-column property="name" label="姓名"
                                             width="200"></el-table-column>
                            <el-table-column property="email" label="邮箱"
                                             width="250"></el-table-column>
                            <el-table-column property="phone"
                                             label="手机" width="250"></el-table-column>
                            <el-table-column property="wechat"
                                             label="微信"></el-table-column>
                            <el-table-column property="state"
                                             label="状态"></el-table-column>
                        </el-table>
                        <el-form ref="form" :model="duanxin_form"
                                 style="margin-top: 40px">
                            <el-form-item label="手机号码" style="margin-bottom: 10px">
                                <el-input v-model="duanxin_form.phone_num"
                                          style="width: 60%;margin-left: 30px"></el-input>
                            </el-form-item>
                            <div style="margin-bottom: 10px">
                                <i class="fa fa-lightbulb-o"
                                   style="color:orange;margin-left: 99px;font-size: 25px;"></i>
                                <span style="margin-left: 5px">直接填写手机号！多个号码请用'.'分割,如13511112222. 13533336666</span>
                            </div>
                            <el-form-item label="推送内容" style="margin-bottom: 10px">
                                <el-input v-model="duanxin_form.content" :disabled="true"
                                          placeholder="新增关注信息，请您点击阅读:thhp//new.yqt365.com/wap/ipouzo00"
                                          style="width: 60%;margin-left: 30px"></el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
                                                        <div style="text-align:center">
                                                            <el-button type="success"
                                                                       style="box-shadow: 1px 1px 1px #ffa108;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: orange;
                                                                   text-align: center"
                                                                       size="mini"
                                                                       @click="duanxin_tongxunlu = false">确定
                                                        </el-button>
                                                        <el-button @click="duanxin_tongxunlu = false"
                                                                   style="box-shadow: 1px 1px 1px grey;margin-left: 30px;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取消
                                                        </el-button>
                                                            <el-button type="success"
                                                                       style="margin-left:30px;box-shadow: 1px 1px 1px #376e00;margin-right: 10px;width: 125px;border-color: transparent;background-color: #32a314"
                                                                       size="small"
                                                                       @click="xinzeng_tongxunlu = true">添加新用户
                                                            </el-button>
                                                        </div>
                                                    </span>
                    </el-dialog>
                    <el-dialog
                            title="新增通讯录"
                            :visible.sync="xinzeng_tongxunlu"
                            width="40%"
                            class="xinzengtongxunlu_dialog">
                        <el-form ref="form" :model="xinzengtongxunlu_form">
                            <el-form-item>
                                <el-input
                                        placeholder="请输入姓名"
                                        prefix-icon="fa fa-user"
                                        v-model="xinzengtongxunlu_form.name">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入邮箱地址"
                                        prefix-icon="fa fa-address-book"
                                        v-model="xinzengtongxunlu_form.email">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入手机号码"
                                        prefix-icon="el-icon-mobile-phone"
                                        v-model="xinzengtongxunlu_form.phone">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入微信号"
                                        prefix-icon="fa fa-comments"
                                        v-model="xinzengtongxunlu_form.wechat">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入单位名称"
                                        prefix-icon="fa fa-building"
                                        v-model="xinzengtongxunlu_form.workplace">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入备注信息"
                                        prefix-icon="fa fa-tag"
                                        v-model="xinzengtongxunlu_form.note">
                                </el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
                                                        <div style="text-align:center">
                                                            <el-button type="success"
                                                                       style="box-shadow: 1px 1px 1px #ffa108;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: orange;
                                                                   text-align: center"
                                                                       size="mini"
                                                                       @click="xinzeng_tongxunlu = false">确认
                                                            </el-button>
                                                            <el-button @click="xinzeng_tongxunlu = false"
                                                                       style="box-shadow: 1px 1px 1px grey;margin-left: 30px;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                       size="mini">取消
                                                            </el-button>
                                                        </div>
                                                    </span>
                    </el-dialog>
                    <el-tooltip class="item" effect="dark" content="删除"
                                placement="bottom">
                        <el-button type="info" style="padding: 4px 4px;"
                                   @click="piliang_shanchuxinxi=true">
                            <d2-icon-svg name="delete1"
                                         style="width: 14px; height: 13px;color: white;fill: white;"/>
                        </el-button>
                    </el-tooltip>
                    <el-dialog
                            title="删除信息"
                            :visible.sync="piliang_shanchuxinxi"
                            width="10%"
                            class="sucaicaozuo_dialog"
                            style="margin-top: 45vh;">
                        <span>确定要删除信息吗？</span>
                        <span slot="footer" class="dialog-footer">
                                                        <el-button type="success"
                                                                   style="box-shadow: 1px 1px 1px #376e00;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #32a314;
                                                                   text-align: center"
                                                                   size="mini"
                                                                   @click="piliang_shanchuxinxi = false">确定
                                                        </el-button>
                                                        <el-button @click="piliang_shanchuxinxi = false"
                                                                   style="box-shadow: 1px 1px 1px grey;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取 消
                                                        </el-button>
                                                    </span>
                    </el-dialog>

                    <el-tooltip class="item" effect="dark" content="标已读"
                                placement="bottom" style="margin-left: 10px">
                        <el-button type="info" style="padding: 4px 4px;"
                                   @click="markAllRead">
                            <d2-icon-svg name="eyecolse"
                                         style="width: 14px; height: 13px;color: white;fill: white;"/>
                        </el-button>
                    </el-tooltip>
                    <el-tooltip class="item" effect="dark" content="导出" placement="bottom">
                        <el-button type="info" style="padding: 4px 4px; ">
                            <i class="fa fa-sign-out" aria-hidden="true"
                               style="width: 14px;height: 13px"></i>
                        </el-button>
                    </el-tooltip>
                    <el-tooltip class="item" effect="dark" content="全选信息加入简报素材（最多1000条）"
                                placement="bottom">
                        <el-button type="info" style="padding: 4px 4px; ">
                            <i class="fa fa-upload" aria-hidden="true"
                               style="width: 14px;height: 13px"></i>
                        </el-button>
                    </el-tooltip>
                </div>
                <div style="float: left;margin-left: 100px;">

                    <el-pagination
                            small
                            background
                            layout="total, prev, pager, next"
                            :total="infolist_count"
                            :page-size="pagination.pageSize"
                            :current-page="pagination.currentPage"
                            @current-change="nextPage"
                    >
                    </el-pagination>
                </div>
                <div style="float: right">
                    <el-input v-model="input" placeholder="在结果中搜索，支持单个词组" size="mini"
                              style="width: 280px;"></el-input>
                    <el-button type="success" size="mini" style="margin-left: 10px;">搜索
                    </el-button>
                </div>
            </div>
        </td>
    </tr>
    <tr v-for="item in infolist">
        <!--checkbox-->
        <td style="width: 20px;">
            <div class="choose">
                <el-checkbox v-model="item.fields.is_checked"
                             @change="chooseInfo(item.pk)"></el-checkbox>
            </div>
        </td>
        <!--头像-->
        <td style="width: 40px;position: relative; border-left: none;border-right: none; ">
            <div>
                <img src="./img/a.png" alt="头像"
                     style="width: 40px; height: 40px; position: absolute; top: 10px;">
            </div>
        </td>


        <td style="border-left: none; display: flex; flex-flow: column nowrap;">
            <div style="display: flex; flex-flow: row nowrap;justify-content: space-between; align-items: center">
                <div style="line-height: 30px; margin-bottom: 10px; position: relative; bottom: -5px; display: flex; flex-flow: row nowrap;justify-content: flex-start;align-items: baseline;">
                    <!--用户名-->
                    <h4 style="display: inline-block; margin: 0 20px 0 0; color: #6699cc">
                        {{item.fields.author_name}}
                    </h4>

                    <div style="height: 28px; display: flex; align-items: baseline;">
                        <!--敏感性-->
                        <el-button type="success" size="mini" style="height: 27px;" v-if="item.fields.sensitive_state"
                                   @click="subChangeSensitive">非敏感
                        </el-button>

                        <el-button type="danger" size="mini" style="height: 27px;" v-else
                                   @click="subChangeSensitive">敏感
                        </el-button>
                        <!--方向性-->
                        <div style="position: relative; display: inline-block; height: 27px;">
                            <el-select class="feeling_select" v-model="item.fields.feelings" size="mini" style="height: 27px;">
                                <el-option label="正面" value=1>正面</el-option>
                                <el-option label="负面" value=2>负面</el-option>
                                <el-option label="中性" value=3>中性</el-option>
                            </el-select>

                            <el-button v-if="item.fields.feelings=== 1"
                                       style="position: absolute; left: 13px; top: 2px; background-color: #67c23a; color: #fff;height: 27px;"
                                       size="mini">正面
                            </el-button>
                            <el-button v-if="item.fields.feelings === 2"
                                       style="position: absolute; left: 13px; top: 2px; background-color: #f56c6c; color: #fff;height: 27px;"
                                       size="mini">负面
                            </el-button>
                            <el-button v-if="item.fields.feelings === 3"
                                       style="position: absolute; left: 13px; top: 2px; background-color: #909399; color: #fff;height: 27px; "
                                       size="mini">中性
                            </el-button>
                        </div>

                        <!--危险性-->
                        <div style="position: relative; bottom: -1px; display: inline-block; height: 27px;">
                            <el-select class="warning_select" v-model="item.fields.warning_level" size="mini"
                                       style="color: #000!important;height: 27px;">
                                <el-option label="高危预警" value='1' style="color:#f56c6c;">高危预警
                                </el-option>
                                <el-option label="中危预警" value='2' style="color:#e6a23c;">中危预警
                                </el-option>
                                <el-option label="低危预警" value='3' style="color:#3a8ee6;">低危预警
                                </el-option>
                            </el-select>

                            <el-button v-if="item.fields.warning_level === '1'"
                                       style="position: relative; left: -115px; top: -1px; background-color: #f56c6c; color: #fff;height: 27px;"
                                       size="mini">高危预警
                            </el-button>
                            <el-button v-if="item.fields.warning_level === '2'"
                                       style="position: relative; left: -115px; top: -1px; background-color: #e6a23c; color: #fff;height: 27px;"
                                       size="mini">中危预警
                            </el-button>
                            <el-button v-if="item.fields.warning_level === '3'"
                                       style="position: relative; left: -115px; top: -1px; background-color: #3a8ee6; color: #fff;height: 27px;"
                                       size="mini">低危预警
                            </el-button>
                        </div>

                    </div>

                </div>
                <!--原创性-->
                <div style="background-color: #a1becc; width: 25px;height: 25px;text-align: center;">
                    <span style="color: white;" v-if="item.article_source">原</span>
                    <span style="color: #7c8084; " v-else>转</span>
                </div>

            </div>

            <!--文章内容-->
            <div>
                <p style="display: inline-block; font-size: 14px; color: grey; margin-top: 10px;margin-right: 50px; display: flex; flex-flow: wrap; ">
                    {{item.fields.content}}
                </p>
            </div>

            <!--附属信息-->
            <div style="display: flex; flex-flow: row nowrap; justify-content: space-between;">
                <div style="display: inline-block;display: flex; flex-flow: column nowrap;">

                    <!--涉及词-->
                    <div style="font-size: 14px; margin-top: 20px;">
                        <span>涉及词：</span>
                        <span style="color: orangered">{{item.fields.key_word}}</span>
                    </div>
                    <!--新源区域 信息类别-->
                    <div style="font-size: 14px;">
                        <span>信源区域：</span>
                        <span style="color: #6699cc">{{item.fields.article_province}}</span>
                        &nbsp;&nbsp;&nbsp;
                        <span>分类：</span>
                        <span style="color: #6699cc">{{item.fields.type}}</span>
                    </div>
                </div>
                <div class="pull-right"
                     style="display: flex; flex-flow: row nowrap; justify-content: flex-start; align-self: flex-end; align-items: center; ">
                    <!--子组件添加jiarushoucangjia属性jiarujianbaosucai属性duanxin_tongxunlu属性youxiang_tongxunlu属性wechat_tongxunlu属性-->
                    <!--按钮集合-->
                    <el-tooltip class="item" effect="dark" content="加入收藏夹"
                                placement="bottom">
                        <el-button type="info" style="padding: 4px 4px;"
                                   @click="jiarushoucangjia=true">
                            <d2-icon-svg name="like"
                                         style="width: 14px; height: 13px;color: white;fill: white;align-items: center"/>
                        </el-button>
                    </el-tooltip>
                    <el-tooltip class="item" effect="dark" content="加入简报素材"
                                placement="bottom">
                        <el-button type="info" style="padding: 4px 4px;"
                                   @click="jiarujianbaosucai=true">
                            <d2-icon-svg name="tag"
                                         style="width: 14px; height: 13px;color: white;fill: white;"/>
                        </el-button>
                    </el-tooltip>


                    <el-dropdown style="margin-left: 10px;margin-right: 10px" size="mini">
                                                    <span class="el-dropdown-link">
                                                        <el-button type="info" style="padding: 4px 4px; ">
                                                            <d2-icon-svg name="share"
                                                                         style="width: 14px; height: 13px;color: white;fill: white;"/>
                                                            <i class="el-icon-arrow-down el-icon--right"
                                                               style="margin-left: 1px;font-size: 1px"></i>
                                                        </el-button>
                                                    </span>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item>
                                <el-tooltip class="item" effect="dark" content="短信发送舆情"
                                            placement="right">
                                    <i class="fa fa-mobile-phone"
                                       style="font-size: 30px"
                                       @click="duanxin_tongxunlu=true"></i>
                                </el-tooltip>
                            </el-dropdown-item>
                            <el-dropdown-item>
                                <el-tooltip class="item" effect="dark" content="邮件发送舆情"
                                            placement="right">
                                    <i class="fa fa-envelope"
                                       style="font-size: 15px"
                                       @click="youxiang_tongxunlu=true"></i>
                                </el-tooltip>
                            </el-dropdown-item>
                            <el-dropdown-item>
                                <el-tooltip class="item" effect="dark" content="微信分享舆情"
                                            placement="right">
                                    <i class="fa fa-weixin"
                                       style="font-size: 16px"
                                       @click="wechat_tongxunlu=true"></i>
                                </el-tooltip>
                            </el-dropdown-item>
                            <el-dropdown-item>
                                <el-tooltip class="item" effect="dark" content="QQ分享舆情"
                                            placement="right">
                                    <i class="fa fa-qq" style="font-size: 16px"></i>
                                </el-tooltip>
                            </el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                    <el-dialog
                            title="素材操作"
                            :visible.sync="jiarushoucangjia"
                            width="10%"
                            class="sucaicaozuo_dialog"
                            style="margin-top: 45vh;">
                        <span>您已选择1个新闻，确认要加入到收藏夹吗？</span>
                        <span slot="footer" class="dialog-footer">
                                                        <el-button type="success"
                                                                   style="box-shadow: 1px 1px 1px #376e00;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #32a314;
                                                                   text-align: center"
                                                                   size="mini"
                                                                   @click="jiarushoucangjia = false">确定
                                                        </el-button>
                                                        <el-button @click="jiarushoucangjia = false"
                                                                   style="box-shadow: 1px 1px 1px grey;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取消
                                                        </el-button>
                                                    </span>
                    </el-dialog>
                    <el-dialog
                            title="素材操作"
                            :visible.sync="piliang_jiarujianbaosucai"
                            width="10%"
                            class="sucaicaozuo_dialog"
                            style="margin-top: 45vh;">
                        <span>您已选择{{news_number}}个新闻，确认要加入到素材库吗？</span>
                        <span slot="footer" class="dialog-footer">
                                                        <el-button type="success"
                                                                   style="box-shadow: 1px 1px 1px #376e00;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #32a314;
                                                                   text-align: center"
                                                                   size="mini"
                                                                   @click="piliang_jiarujianbaosucai = false">确定
                                                        </el-button>
                                                        <el-button @click="piliang_jiarujianbaosucai = false"
                                                                   style="box-shadow: 1px 1px 1px grey;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取 消
                                                        </el-button>
                                                    </span>
                    </el-dialog>
                    <el-dialog
                            title="素材操作"
                            :visible.sync="jiarujianbaosucai"
                            width="10%"
                            class="sucaicaozuo_dialog"
                            style="margin-top: 45vh;">
                        <span>您已选择1个新闻，确认要加入到素材库吗？</span>
                        <span slot="footer" class="dialog-footer">
                                                        <el-button type="success"
                                                                   style="box-shadow: 1px 1px 1px #376e00;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #32a314;
                                                                   text-align: center"
                                                                   size="mini"
                                                                   @click="jiarujianbaosucai = false">确定
                                                        </el-button>
                                                        <el-button @click="jiarujianbaosucai = false"
                                                                   style="box-shadow: 1px 1px 1px grey;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取 消
                                                        </el-button>
                                                    </span>
                    </el-dialog>
                    <el-dialog
                            title="联系人来自通讯录"
                            :visible.sync="duanxin_tongxunlu"
                            width="60%"
                            class="tongxunlu_dialog"
                    >
                        <el-table :data="tongxunluData">
                            <el-table-column property="name" label="姓名"
                                             width="200"></el-table-column>
                            <el-table-column property="email" label="邮箱"
                                             width="250"></el-table-column>
                            <el-table-column property="phone"
                                             label="手机" width="250"></el-table-column>
                            <el-table-column property="wechat"
                                             label="微信"></el-table-column>
                            <el-table-column property="state"
                                             label="状态"></el-table-column>
                        </el-table>
                        <el-form ref="form" :model="duanxin_form"
                                 style="margin-top: 40px">
                            <el-form-item label="手机号码" style="margin-bottom: 10px">
                                <el-input v-model="duanxin_form.phone_num"
                                          style="width: 60%;margin-left: 30px"></el-input>
                            </el-form-item>
                            <div style="margin-bottom: 10px">
                                <i class="fa fa-lightbulb-o"
                                   style="color:orange;margin-left: 99px;font-size: 25px;"></i>
                                <span style="margin-left: 5px">直接填写手机号！多个号码请用'.'分割,如13511112222. 13533336666</span>
                            </div>
                            <el-form-item label="推送内容" style="margin-bottom: 10px">
                                <el-input v-model="duanxin_form.content" :disabled="true"
                                          placeholder="新增关注信息，请您点击阅读:thhp//new.yqt365.com/wap/ipouzo00"
                                          style="width: 60%;margin-left: 30px"></el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
                                                        <div style="text-align:center">
                                                            <el-button type="success"
                                                                       style="box-shadow: 1px 1px 1px #ffa108;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: orange;
                                                                   text-align: center"
                                                                       size="mini"
                                                                       @click="duanxin_tongxunlu = false">确定
                                                        </el-button>
                                                        <el-button @click="duanxin_tongxunlu = false"
                                                                   style="box-shadow: 1px 1px 1px grey;margin-left: 30px;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取消
                                                        </el-button>
                                                            <el-button type="success"
                                                                       style="margin-left:30px;box-shadow: 1px 1px 1px #376e00;margin-right: 10px;width: 125px;border-color: transparent;background-color: #32a314"
                                                                       size="small"
                                                                       @click="xinzeng_tongxunlu = true">添加新用户
                                                            </el-button>
                                                        </div>
                                                    </span>
                    </el-dialog>
                    <el-dialog
                            title="新增通讯录"
                            :visible.sync="xinzeng_tongxunlu"
                            width="40%"
                            class="xinzengtongxunlu_dialog">
                        <el-form ref="form" :model="xinzengtongxunlu_form">
                            <el-form-item>
                                <el-input
                                        placeholder="请输入姓名"
                                        prefix-icon="fa fa-user"
                                        v-model="xinzengtongxunlu_form.name">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入邮箱地址"
                                        prefix-icon="fa fa-address-book"
                                        v-model="xinzengtongxunlu_form.email">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入手机号码"
                                        prefix-icon="el-icon-mobile-phone"
                                        v-model="xinzengtongxunlu_form.phone">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入微信号"
                                        prefix-icon="fa fa-comments"
                                        v-model="xinzengtongxunlu_form.wechat">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入单位名称"
                                        prefix-icon="fa fa-building"
                                        v-model="xinzengtongxunlu_form.workplace">
                                </el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input
                                        placeholder="请输入备注信息"
                                        prefix-icon="fa fa-tag"
                                        v-model="xinzengtongxunlu_form.note">
                                </el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
                                                        <div style="text-align:center">
                                                            <el-button type="success"
                                                                       style="box-shadow: 1px 1px 1px #ffa108;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: orange;
                                                                   text-align: center"
                                                                       size="mini"
                                                                       @click="xinzeng_tongxunlu = false">确认
                                                            </el-button>
                                                            <el-button @click="xinzeng_tongxunlu = false"
                                                                       style="box-shadow: 1px 1px 1px grey;margin-left: 30px;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                       size="mini">取消
                                                            </el-button>
                                                        </div>
                                                    </span>
                    </el-dialog>


                    <el-dialog
                            title="联系人来自通讯录"
                            :visible.sync="youxiang_tongxunlu"
                            width="60%"
                            class="tongxunlu_dialog"
                    >
                        <el-table :data="tongxunluData">
                            <el-table-column property="name" label="姓名"
                                             width="200"></el-table-column>
                            <el-table-column property="email" label="邮箱"
                                             width="250"></el-table-column>
                            <el-table-column property="phone"
                                             label="手机" width="250"></el-table-column>
                            <el-table-column property="wechat"
                                             label="微信"></el-table-column>
                            <el-table-column property="state"
                                             label="状态"></el-table-column>
                        </el-table>
                        <el-form ref="form" :model="email_form"
                                 style="margin-top: 40px">
                            <el-form-item label="邮箱地址" style="margin-bottom: 10px">
                                <el-input v-model="email_form.email"
                                          style="width: 60%;margin-left: 30px"></el-input>
                            </el-form-item>
                            <div style="margin-bottom: 10px">
                                <i class="fa fa-lightbulb-o"
                                   style="color:orange;margin-left: 99px;font-size: 25px;"></i>
                                <span style="margin-left: 5px">直接填写邮箱地址！多个地址请用,分割如test@xd-tech.cn.mail@xd-tech.c</span>
                            </div>
                            <el-form-item label="推送内容" style="margin-bottom: 10px">
                                <el-input v-model="email_form.content"
                                          placeholder="新增关注信息，请您点击阅读:thhp//new.yqt365.com/wap/ipouzo00"
                                          style="width: 60%;margin-left: 30px"></el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
                                                        <div style="text-align:center">
                                                            <el-button type="success"
                                                                       style="box-shadow: 1px 1px 1px #ffa108;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: orange;
                                                                   text-align: center"
                                                                       size="mini"
                                                                       @click="youxiang_tongxunlu = false">确定
                                                        </el-button>
                                                        <el-button @click="youxiang_tongxunlu = false"
                                                                   style="box-shadow: 1px 1px 1px grey;margin-left: 30px;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取消
                                                        </el-button>
                                                            <el-button type="success"
                                                                       style="margin-left:30px;box-shadow: 1px 1px 1px #376e00;margin-right: 10px;width: 125px;border-color: transparent;background-color: #32a314"
                                                                       size="small"
                                                                       @click="xinzeng_tongxunlu = true">添加新用户
                                                            </el-button>
                                                        </div>
                                                    </span>
                    </el-dialog>

                    <el-dialog
                            title="联系人来自通讯录"
                            :visible.sync="wechat_tongxunlu"
                            width="60%"
                            class="tongxunlu_dialog"
                    >
                        <el-table :data="tongxunluData">
                            <el-table-column property="name" label="姓名"
                                             width="200"></el-table-column>
                            <el-table-column property="email" label="邮箱"
                                             width="250"></el-table-column>
                            <el-table-column property="phone"
                                             label="手机" width="250"></el-table-column>
                            <el-table-column property="wechat"
                                             label="微信"></el-table-column>
                            <el-table-column property="state"
                                             label="状态"></el-table-column>
                        </el-table>
                        <el-form ref="form" :model="wechat_form"
                                 style="margin-top: 40px">
                            <el-form-item label="推送内容" style="margin-bottom: 10px">
                                <el-input v-model="wechat_form.content"
                                          placeholder="新增关注信息，请您点击阅读:thhp//new.yqt365.com/wap/ipouzo00"
                                          style="width: 60%;margin-left: 30px"></el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
                                                        <div style="text-align:center">
                                                            <el-button type="success"
                                                                       style="box-shadow: 1px 1px 1px #ffa108;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: orange;
                                                                   text-align: center"
                                                                       size="mini"
                                                                       @click="wechat_tongxunlu = false">确定
                                                        </el-button>
                                                        <el-button @click="wechat_tongxunlu = false"
                                                                   style="box-shadow: 1px 1px 1px grey;margin-left: 30px;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取消
                                                        </el-button>
                                                            <el-button type="success"
                                                                       style="margin-left:30px;box-shadow: 1px 1px 1px #376e00;margin-right: 10px;width: 125px;border-color: transparent;background-color: #32a314"
                                                                       size="small"
                                                                       @click="xinzeng_tongxunlu = true">添加新用户
                                                            </el-button>
                                                        </div>
                                                    </span>
                    </el-dialog>
                    <el-tooltip class="item" effect="dark" content="删除"
                                placement="bottom">
                        <el-button type="info" style="padding: 4px 4px;"
                                   @click="shanchuxinxi=true">
                            <d2-icon-svg name="delete1"
                                         style="width: 14px; height: 13px;color: white;fill: white;"/>
                        </el-button>
                    </el-tooltip>
                    <el-dialog
                            title="删除信息"
                            :visible.sync="shanchuxinxi"
                            width="10%"
                            class="sucaicaozuo_dialog"
                            style="margin-top: 45vh;">
                        <span>确定要删除信息吗？</span>
                        <span slot="footer" class="dialog-footer">
                                                        <el-button type="success"
                                                                   style="box-shadow: 1px 1px 1px #376e00;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #32a314;
                                                                   text-align: center"
                                                                   size="mini"
                                                                   @click="shanchuxinxi = false">确定
                                                        </el-button>
                                                        <el-button @click="shanchuxinxi = false"
                                                                   style="box-shadow: 1px 1px 1px grey;
                                                                   width: 50px;
                                                                   border-color: transparent;
                                                                   background-color: #d1d1d1;
                                                                   text-align: center;
                                                                   color: gray()"
                                                                   size="mini">取 消
                                                        </el-button>
                                                    </span>
                    </el-dialog>
                    <el-tooltip class="item" effect="dark" content="查看原文"
                                placement="bottom" style="margin: 10px 10px;">
                        <a v-bind:href="item.url"
                           target="_blank">
                            <el-button type="info" style="padding: 4px 4px;">
                                <d2-icon-svg name="link"
                                             style="width: 14px; height: 13px;color: white;fill: white;"/>
                            </el-button>
                        </a>

                    </el-tooltip>
                    <el-tooltip class="item" effect="dark" content="标已读"
                                placement="bottom">
                        <el-button type="info" style="padding: 4px 4px;"
                                   v-if="item.is_read ===false"
                                   @click="subChangeReadState">
                            <d2-icon-svg name="eyecolse"
                                         style="width: 14px; height: 13px;color: white;fill: white;"/>
                        </el-button>
                        <el-button type="info"
                                   style="padding: 4px 4px;background-color: orange" v-else
                                   @click="subChangeReadState">
                            <i class="el-icon-view"
                               style="width: 14px;height: 13px;color: white;fill: white"></i>
                        </el-button>
                    </el-tooltip>
                </div>
            </div>
        </td>
        <!--<info-list-item-detail @onload="curent_infoitem"  :item="item"  @subChange_ReadState="change_readState"-->
        <!--@subChange_Sensitive="changeSensitive"></info-list-item-detail>-->
        <!--相似文章数-->
        <td style="font-size: 14px; width: 25px; text-align: center;color: #6699cc">
            {{item.fields.similar_article}}
        </td>
        <!--来源-->
        <td style="font-size: 14px; width: 80px; text-align: center; color: #6699cc">
            {{item.fields.source}}
        </td>
        <!--时间-->
        <td style="text-align: center; font-size: 14px;">{{item.fields.time}}</td>
    </tr>
    </tbody>
</template>

<script>
    export default {
        name: "yq-main-infolist-table",
        props: ['infolist', 'infolist_count'],
        data() {
            return {
                list: [],
                pagination: {
                    currentPage: 1,
                    pageSize: 30,
                },
                checked: false,
                piliang_jiarushoucangjia: false,
                piliang_jiarujianbaosucai: false,
                jiarushoucangjia: false,
                jiarujianbaosucai: false,
                duanxin_form: {
                    phone_num: '',
                    content: '',
                },

                tongxunluData: [{
                    name: '王明',
                    email: '1231241@163.com',
                    phone: '13882140944',
                    wechat: 'sad214',
                    state: '',
                }, {
                    name: '李小刚',
                    email: '1234211241@163.com',
                    phone: '1383255344',
                    wechat: 'sfhad2',
                    state: '',
                }],
                xinzeng_tongxunlu: false,
                duanxin_tongxunlu: false,
                piliang_shanchuxinxi: false,

                youxiang_tongxunlu: false,
                wechat_tongxunlu: false,
                email_form: {
                    email: '',
                    content: '',
                },
                wechat_form: {
                    content: '',
                },
                xinzengtongxunlu_form: {
                    name: '',
                    email: '',
                    phone: '',
                    wechat: '',
                    workplace: '',
                    note: '',
                },

                shanchuxinxi: false,
            }
        },
        methods: {
            nextPage(val) {
                this.pagination.currentPage = val;
                this.$emit('nextPage', this.pagination.currentPage)
                console.log("table this.infolist", this.infolist)
            },
            subChangeSensitive() {
                this.$emit('subChange_Sensitive', this.item.id);

            },
            subChangeReadState() {
                this.$emit('subChange_ReadState', this.item.id);

            },


            // change_readState(id) {
            //     axios.post('/api/info/readstate_change', {
            //         'id': id
            //     }).then(r => {
            //         console.log('response %o', r)
            //         if (r.data.code === 0) {
            //             // this.infolist = r.data.infolist
            //             let info = this.infolist.find(e => e.id === id)
            //             let index = this.infolist.indexOf(info)
            //             this.infolist[index]['is_read'] = !this.infolist[index]['is_read']
            //         }
            //     }).catch(err => {
            //         console.log('error %o', err)
            //     })
            // },
            //


            // changeSensitive(id) {
            //     axios.post('/api/info/sensitive_change', {
            //         'id': id
            //     }).then(r => {
            //         console.log('response %o', r)
            //         if (r.data.code === 0) {
            //             // this.infolist = r.data.infolist
            //             let info = this.infolist.find(e => e.id === id)
            //             let index = this.infolist.indexOf(info)
            //
            //             this.infolist[index]['sensitive_state'] = !this.infolist[index]['sensitive_state']
            //         }
            //     }).catch(err => {
            //         console.log('error %o', err)
            //     })
            // },


            // chooseInfo(id) {
            //     for (let index in this.infolist) {
            //         if (this.infolist[index].fields.is_checked === false) {
            //             this.checked = false
            //             return
            //         }
            //     }
            //     this.checked = true
            //
            //     // axios.post('/api/info/choose_change', {
            //     //   'id': id
            //     // }).then(r => {
            //     //   console.log('response %o', r)
            //     //   if (r.data.code === 0) {
            //     //     let info = this..find(e => e.id === id)
            //     //     let index = this.infolist.indexOf(info)
            //     //     this.infolist[index]['is_checked'] = !this.infolist[index]['is_checked']
            //     //   }
            //     // })
            // },


            chooseAll() {
                for (let index in this.infolist) {
                    this.infolist[index].fields.is_checked = this.checked
                }
            },

            insert_jianbaosucai() {
                this.piliang_jiarujianbaosucai = true
                let num = 0
                if (this.checked === true) {
                    num = this.infolist.length
                } else {
                    for (let index in this.infolist) {
                        if (this.infolist[index].fields.is_checked === true) {
                            num++
                        }
                    }
                }
                this.news_number = num
            },


            insert_shoucangjia() {
                this.piliang_jiarushoucangjia = true
                let num = 0
                if (this.checked === true) {
                    num = this.infolist.length
                } else {
                    for (let index in this.infolist) {
                        if (this.infolist[index].fields.is_checked === true) {
                            num++
                        }
                    }
                }
                this.news_number = num
            },
            markAllRead() {
                for (let index in this.infolist) {
                    if (this.infolist[index].fields.is_checked) {
                        this.infolist[index].fields.is_read = true
                    }
                }
            },
            curent_infoitem(i) {
                this.item = i;
            },
        },


    }
</script>

<style lang="scss">
    @import "../../../assets/style/page1/yuqing.scss";
</style>
