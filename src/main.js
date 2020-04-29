import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import axios from './utils/axios'
import download from './utils/download'

Vue.prototype.$http = axios
Vue.prototype.$download = download

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
