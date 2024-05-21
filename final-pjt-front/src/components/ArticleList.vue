<template>
  <div class="container">
    <h1>Article List</h1>
    <div>
      <p v-for="article in articleStore.articles" :key="article.pk">
        <RouterLink
          :to="{ name: 'community-detail', params: { article_id: article.id } }"
          >{{ article.title }}</RouterLink
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

<style lang="scss" scoped></style>
