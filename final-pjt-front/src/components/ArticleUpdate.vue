<template>
  <div class="container">
    <h1>게시글 수정</h1>
    <form @submit.prevent="update">
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
        value="수정하기"
      />
    </form>
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/article";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import axios from "axios";

const articleStore = useArticleStore();
const title = ref(null);
const content = ref(null);

const route = useRoute();
const authStore = useAuthStore();

const id = ref(route.params.article_id);

onMounted(() => {
  axios({
    method: "get",
    url: `${articleStore.API_URL}/api/articles/${id.value}/`,
    headers: {
      Authorization: `Token ${authStore.token}`,
    },
  })
    .then((res) => {
      title.value = res.data.title;
      content.value = res.data.content;
    })
    .catch((err) => console.log(err));
});

const update = function () {
  const payload = {
    title: title.value,
    content: content.value,
    article_id: id.value,
    token: authStore.token,
  };
  articleStore.updateArticle(payload);
};
</script>

<style scoped></style>
