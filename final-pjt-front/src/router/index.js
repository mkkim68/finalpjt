import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import ProductView from "@/views/ProductView.vue";
import DepositList from "@/components/DepositList.vue";
import SavingsList from "@/components/SavingsList.vue";
import ExchangeView from "@/views/ExchangeView.vue";
import MapView from "@/views/MapView.vue";
import CommunityView from "@/views/CommunityView.vue";
import ChartView from "@/views/ChartView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import ProfileView from "@/views/ProfileView.vue";
import ArticleDetail from "@/components/ArticleDetail.vue";
import ArticleList from "@/components/ArticleList.vue";
import ArticleForm from "@/components/ArticleForm.vue";
import ArticleUpdate from "@/components/ArticleUpdate.vue";
import ProfileUpdate from "@/components/ProfileUpdate.vue";
import DepositDetail from "@/components/DepositDetail.vue";
import SavingsDetail from "@/components/SavingsDetail.vue";
import { useProductStore } from "@/stores/product";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomeView",
      component: HomeView,
    },
    {
      path: "/product",
      component: ProductView,
      redirect: "/product/deposit",
      children: [
        {
          path: "deposit",
          name: "DepositList",
          component: DepositList,
        },
        {
          path: "savings",
          name: "SavingsList",
          component: SavingsList,
        },
      ],
    },
    {
      path: "/deposit/:fin_prdt_cd",
      name: "DepositDetail",
      component: DepositDetail,
    },
    {
      path: "/savings/:fin_prdt_cd",
      name: "SavingsDetail",
      component: SavingsDetail,
    },
    {
      path: "/exchange",
      name: "ExchangeView",
      component: ExchangeView,
    },
    {
      path: "/map",
      name: "MapView",
      component: MapView,
    },
    {
      path: "/community",
      name: "community",
      redirect: "/community",
      component: CommunityView,
      children: [
        {
          path: "",
          name: "community-list",
          component: ArticleList,
        },
        {
          path: ":article_id",
          name: "community-detail",
          component: ArticleDetail,
        },
        {
          path: "create",
          name: "community-create",
          component: ArticleForm,
        },
        {
          path: ":article_id/update",
          name: "community-update",
          component: ArticleUpdate,
        },
      ],
    },
    {
      path: "/chart",
      name: "ChartView",
      component: ChartView,
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/login",
      name: "LogInView",
      component: LogInView,
    },
    {
      path: "/profile/:user_id",
      children: [
        {
          path: "",
          name: "ProfileView",
          component: ProfileView,
        },
        {
          path: "update",
          name: "ProfileUpdate",
          component: ProfileUpdate,
        },
      ],
    },
  ],
});

router.beforeEach((to, from, next) => {
  const store = useProductStore();
  if (to.name === "~View" && !store.isLogin) {
    window.alert("로그인이 필요합니다.");
    next({ name: "LogInView" });
  } else if (
    (to.name === "SignUpView" || to.name === "LogInView") &&
    store.isLogin
  ) {
    window.alert("이미 로그인이 되어있습니다.");
    next({ name: "ProductView" });
  } else {
    next();
  }
});

export default router;
