<template>
  <div>
    <form @submit.prevent="createComment">
      <label for="content">댓글 작성</label>
      <input id="content" type="text" v-model.trim="content" />
      <input type="submit" value="확인" />
    </form>
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/article";
import { useAuthStore } from "@/stores/auth";
import { ref } from "vue";

const content = ref(null);

const props = defineProps({
  article_id: String,
});

const articleStore = useArticleStore();
const authStore = useAuthStore();

const createComment = function () {
  articleStore.createComment(props.article_id, authStore.token, content.value);
};
</script>

<style scoped></style>
