<template>
  <div class="container">
    <h1>Community Page</h1>
    <RouterLink :to="{ name: 'community-create' }">새 글 작성</RouterLink>
    <RouterLink :to="{ name: 'community' }">게시판</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import { onMounted } from "vue";
import { RouterLink, RouterView } from "vue-router";

onMounted(() => {});
</script>

<style scoped>
.container {
  width: 90%;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
}
</style>
