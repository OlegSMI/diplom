import Vue from 'vue'
import VueRouter from 'vue-router'
import MyParsers from '../views/MyParsers.vue'
import MyTableparse from '../views/MyTableparse.vue'
import MyGraph from '../views/MyGraph.vue'
import MyLocation from '../views/MyLocation.vue'
import AnalizUser from '../views/AnalizUser.vue'
// import LoginForm from '../components/login/LoginForm.vue'

Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    name: 'parsers',
    component: MyParsers
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/MyAbout.vue')
  },
  {
    path: '/tableparse',
    name: 'tableparse',
    component: MyTableparse
  },
  {
    path: '/graph',
    name: 'graph',
    component: MyGraph
  },
  {
    path: '/location',
    name: 'location',
    component: MyLocation
  },
  // {
  //   path: '/',
  //   name: 'login',
  //   component: LoginForm
  // },
  {
    path: '/analizuser/:id',
    name: 'analizuser',
    component: AnalizUser
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
