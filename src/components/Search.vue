<template>
  <el-row :gutter="5"
          type="flex"
          justify="center">
    <el-col :xs="10"
            :sm="10"
            :md="12"
            :lg="16"
            :xl="18">
      <el-input v-model="input"
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
      }
      const { data: res } = await this.$http.post('query/queryInfo', {
        input: this.input,
        type: this.dtype
      })
      if (res.code === 400) {
        this.$message.warning(res.msg)
      } else {
        this.$emit('search', res.data)
      }
    }
  }
}
</script>

<style scoped>
.el-row {
  width: 100%;
}
</style>
