<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
/* 解决element的表格错位问题，只能在App.vue里面生效 */
.el-table--border th.gutter:last-of-type {
    display: block !important;
}
</style>
