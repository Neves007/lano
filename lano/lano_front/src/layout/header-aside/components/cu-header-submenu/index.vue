<template>
  <el-submenu class="cu-menu-subitem" :index="menu.path || uniqueId">
    <template slot="title" class="cu-menu-subitem">{{menu.title || '未命名菜单'}}</template>
    <component class="cu-menu-subitem" :menu="submenu" v-for="(submenu, index) in menu.children" :key="index"
               :index="submenu.path || uniqueId"
               :is="submenu.hasOwnProperty('children')?'cu-header-submenu':'el-menu-item'"
               @click="submenu.hasOwnProperty('children')?undefined:handleClick(submenu.path)">{{submenu.title}}</component>
  </el-submenu>
</template>

<script>
import { uniqueId } from 'lodash'
export default {
  name: 'cu-header-submenu',
  props: {
    menu: {
      type: Object,
      required: false,
      default: () => {}
    }
  },
  data () {
    return {
      uniqueId: uniqueId('cu-header-submenu-empty-')
    }
  },
  methods: {
    handleClick (path) {
      this.$router.push({
        path: path
      })
    }
  }
}
</script>
