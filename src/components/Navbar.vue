<template>
  <el-row type="flex"
          align="middle">
    <el-col :span="8"
            class="title">Tasaka</el-col>
    <el-col :span="8"
            :offset="8"
            class="rightbar">
      <div @click="handleIndex">首页</div>
      <div>肿瘤</div>
      <div>罕见病</div>
      <div>关于</div>
      <el-button size="small"
                 plain>登陆/注册</el-button>
    </el-col>
  </el-row>
</template>

<script>
export default {
  methods: {
    handleIndex() {
      console.log('aaaaa')
    }
  }
}
</script>

<style scoped>
/* background-color: #455A64; */
.el-row {
  background-color: #455a64;
  color: #ffffff;
  width: 100%;
}
.title {
  text-align: center;
  font-size: 30px;
}
.rightbar {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}
.rightbar div {
  cursor: pointer;
}
.el-button {
  border: #607d8b;
}
.el-button:hover {
  color: #ffffff;
  background-color: #607d8b;
  border: #607d8b;
}
</style>
