import axios from 'axios'
axios.defaults.baseURL = 'http://test.sunboyan.cn:1001/api/'

axios.interceptors.request.use(config => {
  config.headers.Authorization = 'Token ' + window.sessionStorage.getItem('token')
  return config
}, error => {
  return Promise.reject(error)
})

axios.interceptors.response.use(
  config => {
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

export default axios
