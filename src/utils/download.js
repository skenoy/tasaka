import axios from 'axios'
const instance = axios.create({
  baseURL: 'http://test.sunboyan.cn:1001/api/',
  headers: { 'Content-Type': 'application/json; application/octet-stream' },
  responseType: 'blob'
})

instance.interceptors.request.use(config => {
  // !!!flask接受的请求token，必须赋值给headers.Authorization的token前面加上|Token |
  config.headers.Authorization = 'Token ' + window.sessionStorage.getItem('token')
  return config
}, error => {
  return Promise.reject(error)
})

instance.interceptors.response.use(
  config => {
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

export default instance
