import { createRouter, createWebHashHistory, RouteRecordRaw, createWebHistory } from 'vue-router'
import HomeView from '@/views/home.vue'
import LoginView from '@/views/login.vue'
import store from '@/store'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: { requiresAuth: false }
  },
  {
    path: '/',
    name: 'home',
    component: HomeView,
    redirect: '/chat',
    meta: { requiresAuth: true },
    children: [{
      path: '/chat',
      name: '',
      component: () => import(/* webpackChunkName: "about" */ '../components/chat/index.vue')
    },]
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

// Navigation guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated;
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    // Redirect to login if route requires auth and user is not authenticated
    next('/login');
  } else if (to.path === '/login' && isAuthenticated) {
    // Redirect to home if user is already authenticated
    next('/');
  } else {
    next();
  }
});

export default router

