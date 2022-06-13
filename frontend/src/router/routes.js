import MyParsers from '../views/MyParsers.vue'
import MyTableparse from '../views/MyTableparse.vue'
import MyGraph from '../views/MyGraph.vue'
import MyLocation from '../views/MyLocation.vue'
import AnalizUser from '../views/AnalizUser.vue'
import MyDiagram from '../views/MyDiagram.vue'
// import LoginForm from '../components/login/LoginForm.vue'

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
      component: AnalizUser,
      props: true
    },
    {
      path: '/locationdiagram',
      name: 'locationdiagram',
      component: MyDiagram,
    },
    {
      path: '/we',
      name: 'we',
      component: () => import('../views/MyComp.vue')
    }
  ]

export default routes