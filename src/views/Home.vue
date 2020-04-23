<template>
  <div>
    <Navbar></Navbar>
    <el-row>
      <el-col :span='24'>
        <router-view />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Navbar from '../components/Navbar'

export default {
  components: {
    Navbar
  }
}
</script>

<style scoped>

</style>
