<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="update" v-if="title">
      <label for="title">제목</label><br />
      <input
        type="text"
        id="title"
        v-model.trim="title"
        placeholder="제목을 입력해주세요."
      /><br />
      <label for="content">내용</label><br />
      <textarea
        type="text"
        id="content"
        v-model.trim="content"
        placeholder="내용을 입력해주세요."
      />
      <br />
      <input type="submit" value="확인~~" />
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

<style lang="scss" scoped></style>
