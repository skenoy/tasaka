<template>
  <el-row>
    <el-col :xs="4"
            :sm="4"
            :md="6"
            :lg="8"
            :xl="8"
            class="title">Tasaka</el-col>
    <el-col :xs="4"
            :sm="4"
            :md="6"
            :lg="8"
            :xl="8"
            class="title">&nbsp;</el-col>
    <el-col :xs="16"
            :sm="16"
            :md="14"
            :lg="12"
            :xl="12"
            class="rightbar">
      <div v-for="(item, index) in tabtitle"
           :key="index"
           @click="handle(index)"
           :class="currentIndex === index ? 'active' : ''">
        {{item}}
      </div>
      <el-button size="small"
                 plain>登陆/注册</el-button>
    </el-col>
  </el-row>
</template>

<script>
export default {
  props: {
    tabtitle: {
      type: Array,
      default: () => ['首页', '肿瘤', '罕见病', '关于']
    }
  },
  data () {
    return {
      currentIndex: 0
    }
  },
  methods: {
    // handleIndex () {
    //   this.$router.push('/index').catch(err => err)
    // },
    // handleCancer () {
    //   this.$router.push('/cancer').catch(err => err)
    // },
    // handleRare () {
    //   this.$router.push('/rare').catch(err => err)
    // },
    // handleAbout () {
    //   this.$router.push('/about').catch(err => err)
    // }
    handle (e) {
      switch (e) {
        case 0:
          this.$router.push('/index').catch(err => err)
          this.currentIndex = e
          break
        case 1:
          this.$router.push('/cancer').catch(err => err)
          this.currentIndex = e
          break
        case 2:
          this.$router.push('/rare').catch(err => err)
          this.currentIndex = e
          break
        case 3:
          this.$router.push('/about').catch(err => err)
          this.currentIndex = e
      }
    }
  }
}
</script>

<style scoped>
/* background-color: #455A64; */
.el-row {
  display: flex;
  align-items: center;
  justify-content: space-around;
  background-color: #455a64;
  color: #ffffff;
  width: 100%;
  position: sticky;
  top: 0;
  z-index: 1;
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
.active {
  color: #009688;
}
</style>
