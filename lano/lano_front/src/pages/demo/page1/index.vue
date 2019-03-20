<template>

        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <el-button type="warning" icon="el-icon-plus" plain>添加分组</el-button>
            <el-button type="warning" icon="el-icon-plus" plain>添加方案</el-button>

            <!--<span>卡片名称</span>-->
            <!--<el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
            <el-input style="padding: 5px 0" placeholder="搜索监测方案或文件夹"
                      prefix-icon="el-icon-search"></el-input>
          </div>

        </el-card>

</template>
<style>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>
<script>

    export default {
        name: 'page1',
        data() {
            return {
                activeName: 'second',
                tableData: [{
                    date: '2016-05-02',
                    name: '王小虎',
                    address: '上海市普陀区金沙江路 1518 弄'
                }, {
                    date: '2016-05-04',
                    name: '王小虎',
                    address: '上海市普陀区金沙江路 1517 弄'
                }, {
                    date: '2016-05-01',
                    name: '王小虎',
                    address: '上海市普陀区金沙江路 1519 弄'
                }, {
                    date: '2016-05-03',
                    name: '王小虎',
                    address: '上海市普陀区金沙江路 1516 弄'
                }]
            }
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            }
        }
    };
</script>
