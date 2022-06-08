import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import BarGraph from "../node_modules/vue-svg-charts/src/components/bar"
// import MyHome from './views/MyHome'

// import axios from 'axios'
Vue.config.productionTip = false

// Vue.prototype.$http = axios
// const token = localStorage.getItem('token')
// if (token) {
//   Vue.prototype.$http.defaults.headers.common['Authorization'] = token
// }

// axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')



Vue.use(BarGraph);

// new Vue({
//   router,
//   store,
//   vuetify,
//   render: h => h(MyHome)
// }).$mount('#app')



