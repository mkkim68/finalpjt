<template>
  <div v-if="article" class="container article">
    <h1 class="title">{{ article.title }}</h1>
    <div>
      <span>
        <RouterLink
          :to="{ name: 'ProfileView', params: { user_id: article.user.id } }"
          >{{ article.user.username }}</RouterLink
        >
      </span>
      |
      <span>
        {{ created_at_year }}년 {{ created_at_month }}월 {{ created_at_date }}일
        {{ created_at_hour }}시 {{ created_at_min }}분 {{ created_at_sec }}초
      </span>
    </div>
    <div class="content-container">
      <p>{{ article.content }}</p>
    </div>
    <div v-if="authStore.info.id === article.user.id">
      <RouterLink
        class="btn btn-warning"
        :to="{ name: 'community-update', params: { article_id: article.id } }"
        >수정</RouterLink
      >
      <button
        class="btn btn-danger"
        @click="articleStore.deleteArticle(id, authStore.token)"
      >
        삭제
      </button>
    </div>
    <div class="like-container">
      <p class="like-count">
        <button
          class="like-button"
          @click="like"
          @mouseover="handleMouseOver"
          @mouseout="handleMouseOut"
        >
          <img
            v-if="like_hover"
            class="icon"
            src="@/assets/like_hover.png"
            alt="like_hover"
          />
          <img
            v-else-if="isLiked"
            class="icon"
            src="@/assets/like_full.png"
            alt="like_full"
          />
          <img v-else class="icon" src="@/assets/like.png" alt="like" />
        </button>
        <span> {{ like_users }}</span>
      </p>
      <p class="comment-count">
        <img
          class="icon comment-icon"
          src="@/assets/comment_icon.png"
          alt="comment"
        />
        <span style="vertical-align: center">{{ comment_count }}</span>
      </p>
    </div>
    <div class="comments" style="margin-top: 10px">
      <div class="comment-form">
        <form @submit.prevent="createComment">
          <div class="input-group mb-3">
            <div class="form-floating">
              <input
                style="margin: 0"
                class="form-control"
                type="text"
                placeholder="Leave a comment here"
                id="floatingInputGroup1"
                v-model.trim="content"
              />
              <label for="floatingInputGroup1">댓글을 작성해주세요.</label>
            </div>
            <input
              class="btn btn-outline-secondary t"
              id="button-addon2"
              type="submit"
              value="확인"
            />
          </div>
        </form>
      </div>
      <div ref="comments" class="comment-list">
        <div v-if="comment_count">
          <p v-for="comment in article.comment_set" :key="comment.id">
            <span class="comment-user"><RouterLink
          :to="{ name: 'ProfileView', params: { user_id: comment.user.id } }"
          >@{{ comment.user.username }}</RouterLink
        >
        {{ comment.created_at.slice(0,10) }} {{ comment.created_at.slice(11,19) }}</span>
            <p class="comment-content">
            {{ comment.content }}</p>
          </p>
        </div>
        <p v-else>첫 댓글을 작성해 보세요!</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute, RouterLink, useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import { useArticleStore } from "@/stores/article";
import { useAuthStore } from "@/stores/auth";
import axios from "axios";
const route = useRoute();
const articleStore = useArticleStore();
const authStore = useAuthStore();
const router = useRouter();

const id = ref(route.params.article_id);
const article = ref(null);
const content = ref(null);
const isLiked = ref(null);
const comment_count = ref(null);
const like_users = ref(null);
const created_at_year = ref(null);
const created_at_month = ref(null);
const created_at_date = ref(null);
const created_at_hour = ref(null);
const created_at_min = ref(null);
const created_at_sec = ref(null);

const comments = ref(null);
const like_hover = ref(null);

const handleMouseOver = function () {
  like_hover.value = true;
};

const handleMouseOut = function () {
  like_hover.value = false;
};

const createComment = function () {
  if (content.value) {
    articleStore.createComment(id.value, authStore.token, content.value);
    const pTag = document.createElement("p");
    const a = document.createElement('a');
    a.setAttribute('href', `profile/${authStore.info.id}`)
    const span = document.createElement('span');
    span.classList.add('comment-user')
    a.innerText=`@${authStore.info.username}`
    span.appendChild(a)
    span.setAttribute('style', 'font-size: 15px;')
    const time = document.createElement('span')
    time.innerText = ' now'
    time.setAttribute('style', 'font-size: 15px;')
    span.appendChild(time)
    pTag.appendChild(span)
    const Pcontent = document.createElement('p')
    Pcontent.innerText = content.value;
    Pcontent.classList.add('comment-content')
    pTag.appendChild(Pcontent)
    comments.value.appendChild(pTag);
    content.value = null;
    comment_count.value += 1;
  } else {
    alert("내용을 입력해주세요");
  }
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
      comment_count.value = res.data.comment_count;
      created_at_year.value = res.data.created_at.slice(0, 4);
      created_at_month.value = res.data.created_at.slice(5, 7);
      created_at_date.value = res.data.created_at.slice(8, 10);
      created_at_hour.value = res.data.created_at.slice(11, 13);
      created_at_min.value = res.data.created_at.slice(14, 16);
      created_at_sec.value = res.data.created_at.slice(17, 19);
      like_users.value = res.data.like_users.length;
      if (res.data.like_users.find((item) => item === authStore.info.id)) {
        isLiked.value = true;
      } else {
        isLiked.value = false;
      }
    })
    .catch((err) => {
      console.log(err);
      if (err.response.statusText == "Unauthorized") {
        alert("로그인 해주세요.");
        router.replace({ name: "LogInView" });
      }
    });
});

const like = function () {
  if (isLiked.value === true) {
    like_users.value -= 1;
  } else {
    like_users.value += 1;
  }
  isLiked.value = !isLiked.value;
  const payload = {
    article_id: id.value,
    token: authStore.token,
  };
  articleStore.updateLike(payload);
};
</script>

<style scoped>
.comment-user {
  font-size: 15px;
}
* {
  margin-bottom: 10px;
}
.icon {
  width: 30px;
  background: white;
  margin: 0px;
  align-items: center;
}
.comment-icon {
  width: 25px;
  margin-right: 5px;
}
.comment-count {
  margin: 0 5px;
}
.like-count {
  margin: 0 5px;
  display: flex;
  align-items: center;
}
.like-count > span {
  margin: 0 !important;
  margin: none;
}
.like-button {
  margin: 0;
}
.btn {
  margin-right: 10px;
  width: 60px;
  font-size: 15px;
}

.content-container {
  background-color: rgb(238, 238, 238);
  padding: 20px;
  border-radius: 10px;
}
.like-container {
  display: flex;
  align-items: center;
  margin: 0;
}
.like-button {
  border: none;
  outline: none;
  background-color: white;
  padding: 0px;
  border-radius: 20px;
}
.article {
  background-color: white;
  border-radius: 20px;
  padding: 20px 30px;
}
</style>
