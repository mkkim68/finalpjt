<template>
  <div class="container">
    <h1>Community Page</h1>
    <RouterLink :to="{ name: 'community-create' }" v-if="authStore.isLogin"
      >새 글 작성</RouterLink
    >
    <RouterLink :to="{ name: 'community' }">게시판</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import { onMounted } from "vue";
import { RouterLink, RouterView } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();
</script>

<style scoped>
.container {
  width: 90%;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
}
</style>
