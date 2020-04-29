import axios from 'axios'
import Vue from 'vue'
// 小程序里面可以https调用，但其他时候只能用http
axios.defaults.baseURL = 'http://test.sunboyan.cn:1001/api/'

let loading

function startLoading () {
  loading = Vue.prototype.$loading({
    lock: true,
    text: '加载中。。。',
    background: 'rgba(0,0,0,0.5)',
    target: document.querySelector('.loading-area') // 设置加载动画区域
  })
}

function endLoading () {
  loading.close()
}
// 合并多个loading
let loadingRequestCount = 0

function showLoading () {
  if (loadingRequestCount === 0) {
    startLoading()
  }
  loadingRequestCount++
}

function hideLoading () {
  if (loadingRequestCount <= 0) return
  loadingRequestCount--
  if (loadingRequestCount === 0) {
    endLoading()
  }
}

axios.interceptors.request.use(config => {
  if (config.url !== 'user/check_token') {
    showLoading()
  }
  config.headers.Authorization = 'Token ' + window.sessionStorage.getItem('token')
  return config
}, error => {
  hideLoading()
  return Promise.reject(error)
})

axios.interceptors.response.use(
  config => {
    hideLoading()
    return config
  },
  error => {
    hideLoading()
    return Promise.reject(error)
  }
)

export default axios
