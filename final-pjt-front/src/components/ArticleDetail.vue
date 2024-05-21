<template>
  <div v-if="article" class="container">
    <h1>{{ article.title }}</h1>
    <p>
      작성자:
      <RouterLink :to="{ name: 'ProfileView', params: { user_id: user_id } }">{{
        author
      }}</RouterLink>
    </p>
    <p>작성 시간: {{ article.created_at }}</p>
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
      <button @click="like">{{ isLiked ? "좋아요 취소" : "좋아요" }}</button>
    </div>
    <div>
      <h3>댓글 {{ article.comment_count }}개</h3>
      <div>
        <form @submit.prevent="createComment">
          <label for="content">댓글 작성</label>
          <input id="content" type="text" v-model.trim="content" />
          <input type="submit" value="확인" />
        </form>
      </div>
      <ul ref="comments">
        <li v-for="comment in article.comment_set" :key="comment.id">
          {{ comment.content }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
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
const content = ref(null);
const isLiked = ref(null);

const comments = ref(null);

const createComment = function () {
  articleStore.createComment(id.value, authStore.token, content.value);
  const liTag = document.createElement("li");
  liTag.innerText = content.value;
  comments.value.appendChild(liTag);
  content.value = null;
};

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
      if (res.data.like_users.find((item) => item === authStore.info.id)) {
        isLiked.value = true;
      } else {
        isLiked.value = false;
      }
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
  isLiked.value = !isLiked.value;
  const payload = {
    article_id: id.value,
    token: authStore.token,
  };
  articleStore.updateLike(payload);
};
</script>

<style lang="scss" scoped></style>
