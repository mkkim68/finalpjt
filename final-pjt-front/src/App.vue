<template>
  <header>
    <nav>
      <div class="menu">
        <span class="logo">
          <RouterLink to="/">
            <img class="icon logo" src="@/assets/logo.png" alt="product"></RouterLink>
        </span>
        <RouterLink :to="{ name: 'ProductView'}">
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
          <RouterLink :to="{ name: 'LogInView'}"><span>로그인</span></RouterLink> | 
          <a class="hi" href=""><span>마이페이지</span></a>
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

  img.icon {
    width: 50px;
  }

  div.menu {
    display: flex;
    align-items: center;
    background-color: #dff7e4;
    border-radius: 20px 0 0 20px;
  }
  div.menu > a {
    display: flex;
    flex-direction: row;
    align-items: center;
    text-decoration: none;
    color: grey;
    font-size: larger;
    font-weight: 530;
    margin: 20px;
    padding: 5px;
    width: 160px;
  }

  div.menu > a > img {
    padding : 0 10px;
  }

  span.logo {
    padding-left: 10px;
  }

  span.user {
    margin-left: auto;
    width: 200px;
  }
  span.user > a {
    text-decoration: none;
    font-size: large;
  }

  a:link, a:visited {
    text-decoration: none;
  }

  a:hover > span {
    color: #13BD7E;
    font-weight: bolder;
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

</style>
