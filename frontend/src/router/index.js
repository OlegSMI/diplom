import Vue from 'vue'
import VueRouter from 'vue-router'
import MyHome from '../views/MyHome.vue'
import MyDick from '../views/MyDick.vue'
import MyProjects from '../views/MyProjects.vue'
import MyLocation from '../views/MyLocation.vue'
import LoginForm from '../components/login/LoginForm.vue'

Vue.use(VueRouter)


const routes = [
  {
    path: '/home',
    name: 'Home',
    component: MyHome
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/MyAbout.vue')
  },
  {
    path: '/Dick',
    name: 'Dick',
    component: MyDick
  },
  {
    path: '/projects',
    name: 'projects',
    component: MyProjects
  },
  {
    path: '/location',
    name: 'location',
    component: MyLocation
  },
  {
    path: '/',
    name: 'login',
    component: LoginForm
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
