<template>
  <div class="container">
    <h1>새 게시글 작성</h1>
    <form @submit.prevent="create">
      <div class="form-floating mb-3">
        <input
          type="text"
          class="form-control"
          id="floatingInput"
          v-model.trim="title"
          placeholder=""
        />
        <label for="floatingInput">제목</label>
      </div>
      <div class="form-floating">
        <input
          class="form-control"
          placeholder="내용을 입력해주세요."
          v-model.trim="content"
          id="content"
          type="text"
          style="height: 100px"
        />
        <label for="content">내용</label>
      </div>
      <input
        style="margin-top: 10px"
        class="btn btn-light"
        type="submit"
        value="확인"
      />
    </form>
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/article";
import { useAuthStore } from "@/stores/auth";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const articleStore = useArticleStore();
const authStore = useAuthStore();
const title = ref(null);
const content = ref(null);
const router = useRouter();
onMounted(() => {
  if (!authStore.isLogin) {
    alert("로그인을 해주세요.");
    router.push({ name: "LogInView" });
  }
});

const create = function () {
  const payload = {
    title: title.value,
    content: content.value,
    token: authStore.token,
  };
  articleStore.createArticle(payload);
};
</script>

<style lang="scss" scoped></style>
