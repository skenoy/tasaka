<template>
  <el-row :gutter="5"
          type="flex"
          justify="center">
    <el-col :xs="10"
            :sm="10"
            :md="12"
            :lg="16"
            :xl="18">
      <el-input v-model.trim="input"
                placeholder="基因 / 疾病 / 药物"
                prefix-icon="el-icon-search"
                @keyup.enter.native="search">
      </el-input>
    </el-col>
    <el-col :span="2">
      <el-button type="primary"
                 icon="el-icon-search"
                 @click="search">搜索</el-button>
    </el-col>
  </el-row>
</template>

<script>
export default {
  props: {
    dtype: String
  },
  data () {
    return {
      input: ''
    }
  },
  methods: {
    async search () {
      if (this.input === '') {
        return this.$message.warning('请输入查询内容！')
      } else if (this.input.length === 1) {
        return this.$message.warning('请输入至少两个字符！')
      }
      await this.$http.post('query/queryInfo', {
        input: this.input,
        type: this.dtype
      }).then(response => {
        const { data: res } = response
        if (res.code === 400) {
          this.$message.warning(res.msg)
        } else if (res.code === 200) {
          this.$message.warning(`剩余搜索次数为：${res.snumber}`)
          this.$emit('search', res.data)
        } else {
          this.$message.warning(`剩余搜索次数为：${res.snumber}`)
          this.$message.warning(res.msg)
        }
      }).catch(() => {
        this.$message.warning('请登录之后搜索！')
      })
    }
  }
}
</script>

<style scoped>
.el-row {
  width: 100%;
}
</style>
