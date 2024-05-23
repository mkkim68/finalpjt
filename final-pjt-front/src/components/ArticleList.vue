<template>
  <div class="container">
    <h1>게시판</h1>
    <div>
      <p
        v-for="article in articleStore.articles"
        :key="article.pk"
        class="list"
      >
        <RouterLink
          :to="{ name: 'community-detail', params: { article_id: article.id } }"
          ><p class="info">{{ article.title }}</p>
          <p class="info user">
            {{ article.user.username }}
            <svg
              class="icon comment"
              enable-background="new 0 0 32 32"
              height="32px"
              id="Layer_1"
              version="1.1"
              viewBox="0 0 32 32"
              width="32px"
              xml:space="preserve"
              xmlns="http://www.w3.org/2000/svg"
              xmlns:xlink="http://www.w3.org/1999/xlink"
            >
              <g>
                <polyline
                  fill="none"
                  points="   649,137.999 675,137.999 675,155.999 661,155.999  "
                  stroke="#FFFFFF"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-miterlimit="10"
                  stroke-width="2"
                />
                <polyline
                  fill="none"
                  points="   653,155.999 649,155.999 649,141.999  "
                  stroke="#FFFFFF"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-miterlimit="10"
                  stroke-width="2"
                />
                <polyline
                  fill="none"
                  points="   661,156 653,162 653,156  "
                  stroke="#FFFFFF"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-miterlimit="10"
                  stroke-width="2"
                />
              </g>
              <path
                d="M29,3H3C2.448,3,2,3.448,2,4c0,0.552,0.448,1,1,1h25v16H15c-0.041,0-0.076,0.018-0.116,0.023  c-0.067,0.008-0.13,0.018-0.195,0.039c-0.068,0.022-0.127,0.053-0.187,0.089c-0.033,0.019-0.071,0.025-0.102,0.049L8,26v-4  c0,0,0,0,0,0s0,0,0,0c0-0.553-0.448-1-1-1H4V8c0-0.552-0.448-1-1-1S2,7.448,2,8V22c0,0.553,0.448,1,1,1h3v5  c0,0.379,0.214,0.725,0.553,0.895C6.694,28.965,6.848,29,7,29c0.212,0,0.423-0.067,0.6-0.2l7.733-5.8H29c0.553,0,1-0.447,1-1V4  C30,3.448,29.553,3,29,3z"
              />
            </svg>

            {{ article.comment_count }}
            <svg
              class="icon"
              viewBox="0 0 512 512"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title />
              <g data-name="1" id="_1">
                <path
                  d="M348.45,432.7H261.8a141.5,141.5,0,0,1-49.52-8.9l-67.5-25.07a15,15,0,0,1,10.45-28.12l67.49,25.07a111.79,111.79,0,0,0,39.08,7h86.65a14.21,14.21,0,1,0,0-28.42,15,15,0,0,1,0-30H368.9a14.21,14.21,0,1,0,0-28.42,15,15,0,0,1,0-30h20.44a14.21,14.21,0,0,0,10.05-24.26,14.08,14.08,0,0,0-10.05-4.16,15,15,0,0,1,0-30h20.45a14.21,14.21,0,0,0,10-24.26,14.09,14.09,0,0,0-10-4.17H268.15A15,15,0,0,1,255,176.74a100.2,100.2,0,0,0,9.2-29.33c3.39-21.87-.79-41.64-12.42-58.76a12.28,12.28,0,0,0-22.33,7c.49,51.38-23.25,88.72-68.65,108a15,15,0,1,1-11.72-27.61c18.72-8,32.36-19.75,40.55-35.08,6.68-12.51,10-27.65,9.83-45C199.31,77,211,61,229.18,55.34s36.81.78,47.45,16.46c24.71,36.36,20.25,74.1,13.48,97.21H409.79a44.21,44.21,0,0,1,19.59,83.84,44.27,44.27,0,0,1-20.44,58.42,44.27,44.27,0,0,1-20.45,58.43,44.23,44.23,0,0,1-40,63Z"
                />
                <path
                  d="M155,410.49H69.13a15,15,0,0,1-15-15V189.86a15,15,0,0,1,15-15H155a15,15,0,0,1,15,15V395.49A15,15,0,0,1,155,410.49Zm-70.84-30H140V204.86H84.13Z"
                />
              </g>
            </svg>
            {{ article.like_users.length }}
          </p>
        </RouterLink>
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
.icon {
  width: 20px;
  height: auto;
  vertical-align: middle;
  margin-left: 5px;
  margin-top: -3px;
}
.comment {
  width: 18px;
}
a {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: start;
  padding: 0px 10px;
  vertical-align: middle;
  text-decoration: none;
}
.list:hover {
  background-color: rgb(235, 255, 233);
}
.list {
  background-color: white;
  padding: 10px;
  margin: 5px;
  border-radius: 10px;
}
.info {
  text-align: center;
  margin: 0;
  font-size: 20px;
  vertical-align: middle;
}
.user {
  font-size: 15px;
  color: gray;
}
</style>
