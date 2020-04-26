<template>
  <div class="index">
    <Search @search="handleSearch"></Search>
    <el-table :data="tableData"
              size="medium"
              border
              v-show="showTable">
      <el-table-column prop="name"
                       label="项目名称" />
      <el-table-column prop="bioid"
                       label="生信编号" />
      <el-table-column prop="difftime"
                       label="剩余时间" />
      <el-table-column prop="ctime"
                       label="完成时间" />
      <el-table-column label="附件"
                       width="50">
        <template slot-scope="scope">
          <el-button size="mini"
                     :disabled="scope.row.fileurl === ''"
                     icon="el-icon-download"
                     circle
                     @click="download(scope.row.fileurl)"></el-button>
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
      tableData: [
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        },
        {
          name: '1',
          bioid: '1',
          difftime: '1',
          ctime: '1',
          fileurl: ''
        }
      ]
    }
  },
  methods: {
    handleSearch () {
      this.showTable = true
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
