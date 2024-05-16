import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ProductView from '@/views/ProductView.vue'
import DepositList from '@/components/DepositList.vue'
import SavingsList from '@/components/SavingsList.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import MapView from '@/views/MapView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ChartView from '@/views/ChartView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import { useCounterStore } from '@/stores/counter'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/product',
      component: ProductView,
      children: [
        { path: '', name: 'ProductView', component: ProductView },
        { path: 'deposit', name: 'DepositList', component: DepositList },
        { path: 'savings', name: 'SavingsList', component: SavingsList },
      ],
      beforeEnter: (to, from) => {
        console.log(to)
        console.log(from)
      } 
    },
    {
      path: '/exchange',
      name: 'ExchangeView',
      component: ExchangeView
    },
    {
      path: '/map',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/community',
      name: 'CommunityView',
      component: CommunityView
    },
    {
      path: '/chart',
      name: 'ChartView',
      component: ChartView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === '~View' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return {name: 'LogInView'}
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인이 되어있습니다.')
    return {name: 'ProductView'}
  }
})

export default router
