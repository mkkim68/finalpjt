<template>
  <header>
    <nav>
      <div class="menu">
        <span class="logo">
          <RouterLink to="/">
            <img class="icon logo" src="@/assets/logo.png" alt="product" />
          </RouterLink>
        </span>
        <RouterLink :to="{ name: 'DepositList' }" active-class="active">
          <img class="icon product" src="@/assets/product.png" alt="product" />
          <span class="link-text">예적금</span>
        </RouterLink>
        <RouterLink :to="{ name: 'ExchangeView' }" active-class="active">
          <img class="icon exchange" src="@/assets/exchange.png" alt="product" />
          <span class="link-text">환율</span>
        </RouterLink>
        <RouterLink :to="{ name: 'MapView' }" active-class="active">
          <img class="icon map" src="@/assets/map.png" alt="product" />
          <span class="link-text">지도</span>
        </RouterLink>
        <RouterLink :to="{ name: 'community' }" active-class="active">
          <img class="icon community" src="@/assets/community.png" alt="product" />
          <span class="link-text">게시판</span>
        </RouterLink>
        <RouterLink :to="{ name: 'ChartView' }" active-class="active">
          <img class="icon chart" src="@/assets/chart.png" alt="product" />
          <span class="link-text">차트</span>
        </RouterLink>

        <span class="user" v-if="!authStore.isLogin">
          <RouterLink :to="{ name: 'SignUpView' }">
            <span>회원가입</span>
          </RouterLink>
          <span> | </span>
          <RouterLink :to="{ name: 'LogInView' }">
            <span>로그인</span>
          </RouterLink>
        </span>
        <span class="user" v-else>
          <RouterLink :to="{ name: 'ProfileView', params: { user_id: authStore.info?.id || 'default' } }" class="hi" v-if="authStore.info">
            <span>{{ authStore.info.username }}님 안녕하세요</span>
          </RouterLink>
          <span> | </span>
          <a @click="authStore.logOut"><span>로그아웃</span></a>
        </span>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { onMounted } from "vue";
import { RouterView, RouterLink } from "vue-router";
import { useAuthStore } from "./stores/auth";
const authStore = useAuthStore();

onMounted(() => {
  console.log("authStore.info: ", authStore.info); // authStore.info 값을 콘솔에 출력
});
</script>

<style scoped>
img.logo {
  width: 80px;
}

img.icon {
  width: 50px;
  margin-right: 0px;
}

img.product {
  width: 45px;
  margin-right: 3px;
}

img.map {
  margin-right: -5px;
}

div.menu {
  background-color: #e4f9e9;
  display: flex;
  align-items: center;
  border-radius: 0 0 10px 10px;
  font-family: "Jua", sans-serif;
  font-weight: 400;
  font-size: 24px;
  font-style: normal;
}

div.menu > a {
  display: flex;
  flex-direction: row;
  align-items: center;
  text-decoration: none;
  color: grey;
  font-size: larger;
  font-weight: 530;
  margin: 20px 0px;
  padding: 5px;
  width: 200px;
}

div.menu > a > span {
  width: 80px;
}

div.menu > a > img {
  padding: 0 5px;
}

span.logo {
  padding-left: 15px;
  margin-right: 30px;
}

span.user > a {
  text-decoration: none;
  color: black;
  font-size: medium;
}

a:link,
a:visited {
  text-decoration: none;
}

a:hover > span {
  color: #13bd7e;
  cursor: pointer;
}

a:active > span {
  font-weight: 2em;
}

a.hi {
  overflow: hidden;
  white-space: nowrap;
  display: inline-block;
}

a.hi:hover span {
  display: inline-block;
  font-weight: bolder;
  opacity: 1;
  animation: waveEffect 3s ease-in-out forwards;
  align-items: center;
}

@keyframes waveEffect {
  0% {
    opacity: 1;
    color: black;
    align-items: center;
  }
  50% {
    opacity: 1;
    color: #5d87ff;
    font-size: 1.2em;
    align-items: center;
  }
  100% {
    opacity: 1;
    color: black;
    align-items: center;
  }
}

.active {
  font-weight: bold;
  color: #4caf50;
}

.link-text {
  color: grey;
}

.active .link-text {
  color: #4caf50;
}

span.user {
  margin: 0px auto;
  min-width: 200px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
</style>
