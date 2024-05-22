<template>
  <div class="container">
    <h1>게시판</h1>
    <div>
      <p v-for="article in articleStore.articles" :key="article.pk">
        <RouterLink
          :to="{ name: 'community-detail', params: { article_id: article.id } }"
          ><span>{{ article.title }}</span
          ><span>댓글: {{ article.comment_count }}</span></RouterLink
        >
      </p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useArticleStore } from "@/stores/article";
import ArticleDetail from "./ArticleDetail.vue";
import { RouterLink } from "vue-router";
const articleStore = useArticleStore();

onMounted(() => {
  articleStore.getArticles();
});
</script>

<style scoped>
a {
  display: flex;
  justify-content: space-between;
  padding: 0px 10px;
  text-decoration: none;
}
p:hover {
  background-color: rgb(235, 235, 235);
}
p {
  background-color: white;
  padding: 10px;
  margin: 5px;
  border-radius: 10px;
  /* border-bottom: 1px solid #4696ff; */
}
</style>
