<template>
  <div v-if="article" class="container">
    <h1>{{ article.title }}</h1>
    <p>
      작성자:
      <RouterLink :to="{ name: 'ProfileView', params: { user_id: user_id } }">{{
        article.user
      }}</RouterLink>
    </p>
    <p>{{ article.content }}</p>
    <div v-if="authStore.info.id === article.user">
      <RouterLink
        :to="{ name: 'community-update', params: { article_id: article.id } }"
        >수정</RouterLink
      >
      <button @click="articleStore.deleteArticle(id, authStore.token)">
        삭제
      </button>
    </div>
    <div>
      <button @click="like">좋아요</button>
    </div>
    <div>
      <h3>댓글 {{ article.comment_count }}개</h3>
      <CommentForm :article_id="id" />
      <p v-for="comment in article.comment_set">{{ comment.content }}</p>
    </div>
  </div>
</template>

<script setup>
import CommentForm from "./CommentForm.vue";
import { useRoute, RouterLink } from "vue-router";
import { ref, onMounted } from "vue";
import { useArticleStore } from "@/stores/article";
import { useAuthStore } from "@/stores/auth";
import axios from "axios";
const route = useRoute();
const articleStore = useArticleStore();
const authStore = useAuthStore();

const id = ref(route.params.article_id);
const article = ref(null);
const author = ref(null);
const user_id = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: `${articleStore.API_URL}/api/articles/${id.value}/`,
    headers: {
      Authorization: `Token ${authStore.token}`,
    },
  })
    .then((res) => {
      article.value = res.data;
      user_id.value = res.data.user;
      axios({
        method: "get",
        url: `${authStore.API_URL}/accounts/${user_id.value}/`,
      })
        .then((response) => {
          author.value = response.data.username;
        })
        .catch((err) => console.log(err));
    })
    .catch((err) => console.log(err));
});

const like = function () {
  const payload = {
    article_id: id.value,
    token: authStore.token,
  };
  articleStore.updateLike(payload);
};
</script>

<style lang="scss" scoped></style>
