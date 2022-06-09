import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

// import axios from 'axios'
Vue.config.productionTip = false

// Vue.prototype.$http = axios
// axios.defaults.baseURL = 'http://127.0.0.1:8000'
// const token = localStorage.getItem('token')
// if (token) {
//   Vue.prototype.$http.defaults.headers.common['Authorization'] = token
// }

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
