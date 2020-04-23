import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    component: () => import('../views/Home'),
    redirect: '/index',
    children: [
      {
        path: '/index',
        component: () => import('../views/Index')
      },
      {
        path: '/cancer',
        component: () => import('../views/Cancer')
      },
      {
        path: '/rare',
        component: () => import('../views/Rare')
      },
      {
        path: '/about',
        component: () => import('../views/About')
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  next()
})

export default router
