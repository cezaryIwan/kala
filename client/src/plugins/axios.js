import axios from 'axios'
import router from '../router' 

const api = axios.create({
  baseURL: 'http://localhost:8000', 
  timeout: 10000,
})

api.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('access_token')
      router.push('/login')
    }
    return Promise.reject(error)
  }
)

export default api
