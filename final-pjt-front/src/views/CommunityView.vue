<template>
  <div class="container">
    <div>
      <RouterLink :to="{ name: 'community' }">게시판</RouterLink>
      <RouterLink :to="{ name: 'community-create' }" v-if="authStore.isLogin"
        >새 글 작성</RouterLink
      >
    </div>
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
a {
  position: relative;
  display: inline-block;
  top: 0;
  right: 0;
  padding: 10px 20px;
  margin: 10px;
  background-color: #ffffff; /* 하늘색 배경 */
  color: #4696ff; /* 흰색 텍스트 */
  border-radius: 20px; /* 라운드한 모양 */
  text-decoration: none;
  box-shadow: #86bbff 2px 3px 1px;
  overflow: hidden; /* 내부 내용이 넘칠 경우를 대비하여 오버플로우 감추기 */
}

/* a 태그 주변에 흰색 불빛 애니메이션 효과 */
a:hover {
  background-color: #f2f8ff;
}
a:active {
  box-shadow: none;
  top: 2px;
  right: -3px;
}
</style>
