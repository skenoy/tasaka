<template>
  <div class="index">
    <Search @search="handleSearch"
            :dtype="disease"></Search>
    <el-table :data="tableData"
              size="medium"
              border
              v-show="showTable">
      <el-table-column prop="id"
                       width="50"
                       align="center"
                       label="ID" />
      <el-table-column prop="diseasename"
                       label="疾病名称" />
      <el-table-column prop="cause"
                       label="病因" />
      <el-table-column prop="drug"
                       label="疾病用药" />
      <el-table-column prop="approval"
                       label="批准用药" />
      <el-table-column label="详细信息"
                       align="center"
                       width="80">
        <template slot-scope="scope">
          <el-button type="success"
                     size="mini"
                     plain
                     :disabled="scope.row.zhid === ''"
                     icon="el-icon-download"
                     circle
                     @click="download(scope.row.zhid)"></el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import Search from '../components/Search'

export default {
  components: {
    Search
  },
  data () {
    return {
      showTable: false,
      tableData: [],
      disease: 'rare'
    }
  },
  methods: {
    handleSearch (childrenData) {
      this.tableData = childrenData
      this.showTable = true
    },
    async download (fileurl) {
      this.$message.info('正在下载中...请耐心等待！')
      const res = await this.$download.post('query/download', {
        file: fileurl,
        type: this.disease
      })
      const blob = new Blob([res.data])
      const fileName = fileurl
      const urlObject = window.URL || window.webkitURL || window
      const url = urlObject.createObjectURL(blob)
      const el = document.createElement('a')
      el.href = url
      el.download = fileName
      el.click()
      urlObject.revokeObjectURL(url)
      this.$message.success('下载成功！')
    }
  }
}
</script>

<style scoped>
.index {
  min-height: 100vh;
  padding-top: 100px;
  background-color: #607d8b;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.el-table {
  margin: 30px 0;
  width: 75%;
}
</style>
