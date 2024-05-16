<template>
  <div>
    <h1>MainPage</h1>
  </div>

  <header>
    <nav>
      <div>
        <RouterLink :to="{ name: 'ProductView'}">예적금</RouterLink> |
        <RouterLink :to="{ name: 'ExchangeView'}">환율</RouterLink> |
        <RouterLink :to="{ name: 'MapView'}">지도</RouterLink> |
        <RouterLink :to="{ name: 'CommunityView'}">게시판</RouterLink> |
        <RouterLink :to="{ name: 'ChartView'}">차트</RouterLink>
      </div>
      <div>
        <RouterLink :to="{ name: 'SignUpView'}">회원가입</RouterLink> |
        <RouterLink :to="{ name: 'LogInView'}">로그인</RouterLink>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped></style>
