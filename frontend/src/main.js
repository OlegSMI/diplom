import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import BarGraph from "../node_modules/vue-svg-charts/src/components/bar"
// import MyHome from './views/MyHome'

Vue.config.productionTip = false

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



// Vue.prototype.$http = axios;
