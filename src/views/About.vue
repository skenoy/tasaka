<template>
  <div class="index">
    <div class="title">网站技术栈</div>
    <div class="frond">前端：<span>Vue</span><span>VueCli</span><span>Element</span><span>TweenJS</span><span>Axios</span></div>
    <div class="back">后端：<span>Linux</span><span>Nginx</span><span>Gunicorn</span><span>Flask</span><span>Mysql</span><span>&nbsp;</span></div>
    <div class="spider">预先爬虫：<span>pyppeteer</span><span>lxml</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span></div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.index {
  height: 100vh;
  background-color: #607d8b;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.title {
  font-size: 24px;
  color: #ffffff;
  font-weight: 900;
}
.frond {
  margin-top: 5%;
  color: #ffffff;
}
.back {
  margin-top: 5%;
  color: #ffffff;
}
.spider {
  margin-top: 5%;
  color: #ffffff;
}
span {
  margin: 0 5px;
}
</style>
