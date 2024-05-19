<template>
  <header>
    <nav>
      <div class="menu">
        <span class="logo">
          <RouterLink to="/">
            <img class="icon logo" src="@/assets/logo.png" alt="product"></RouterLink>
        </span>
        <RouterLink :to="{ name: 'DepositList'}">
          <img class="icon product" src="@/assets/product.png" alt="product"><span>예적금</span></RouterLink>
        <RouterLink :to="{ name: 'ExchangeView'}">
          <img class="icon exchange" src="@/assets/exchange.png" alt="product"><span>환율</span></RouterLink>
        <RouterLink :to="{ name: 'MapView'}">
          <img class="icon map" src="@/assets/map.png" alt="product"><span>지도</span></RouterLink>
        <RouterLink :to="{ name: 'CommunityView'}">
          <img class="icon community" src="@/assets/community.png" alt="product"><span>게시판</span></RouterLink>
        <RouterLink :to="{ name: 'ChartView'}">
          <img class="icon chart" src="@/assets/chart.png" alt="product"><span>차트</span></RouterLink>
        <span class="user">
          <RouterLink :to="{ name: 'SignUpView'}"><span>회원가입</span></RouterLink> |
          <RouterLink :to="{ name: 'LogInView'}"><span>로그인</span></RouterLink>
          <a class="hi" href=""><span>admin님 안녕하세요</span></a>
        </span>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
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
  font-style:normal;
}

div.menu > a {
  /* border: 1px solid black; */
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
  padding : 0 5px;
}

span.logo {
  padding-left: 15px;
  margin-right: 30px;
}

span.user {
  margin-left: auto;
  width: 200px;
}

span.user > a {
  text-decoration: none;
  color: black;
  font-size: medium;
}

a:link, a:visited {
  text-decoration: none;
}

a:hover > span {
  color: #13BD7E;
}

a:active > span {
  font-weight: 2em;
}


a.hi {
  overflow: hidden;
  white-space: nowrap;
  display : inline-block;
}

a.hi:hover span {
  display: inline-block;
  font-weight : bolder;
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
      color: #5D87FF;
      font-size : 1.2em;
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

</style>
