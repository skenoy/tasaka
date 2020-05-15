<template>
  <div class="index">
    <div class="main">肿瘤/罕见病治疗案例</div>
    <div class="sub">来源--知乎-杀生丸--解读案例</div>
    <div class="sub">1M小水管。。。每天5次搜索，12:00重置？？？</div>
    <div class="sub">不管其为人行事，仅学习其知识</div>
    <div class="number">
      <!-- <div>肿瘤数据：<span>{{cancerNumberTween}}</span></div> -->
      <div>肿瘤数据：<span>{{cancerNumberTween}}</span><br>进度：1000+完成</div>
      <div>罕见病数据：<span>{{rareNumberTween}}</span><br>进度：120完成</div>
    </div>
  </div>
</template>

<script>
import VueMixinTween from 'vue-mixin-tween'

export default {
  data () {
    return {
      cancerNumber: 0,
      rareNumber: 0
    }
  },
  mounted () {
    this.cancerNumber = 112
    this.rareNumber = 36
  },
  mixins: [
    VueMixinTween('cancerNumber', 2000),
    VueMixinTween('rareNumber', 2000)
  ]
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
div {
  color: #ffffff;
}
.main {
  font-size: 64px;
  font-weight: 900;
}
.sub {
  font-size: 24px;
  color: #bdbdbd;
}
.number {
  width: 100%;
  display: flex;
  justify-content: space-evenly;
  margin-top: 3%;
  font-size: 24px;
}
.number span {
  font-size: 48px;
  font-weight: 900;
}
</style>
