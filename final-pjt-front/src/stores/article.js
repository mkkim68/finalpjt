import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import axios from "axios";

export const useArticleStore = defineStore("article", () => {
  const router = useRouter();
  const API_URL = "http://127.0.0.1:8000";
  const articles = ref([]);

  const updateLike = function (payload) {
    const { article_id, token } = payload;
    axios({
      method: "post",
      url: `${API_URL}/api/articles/${article_id}/likes/`,
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => {
        // console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  const getArticles = function () {
    axios({
      method: "get",
      url: `${API_URL}/api/articles/`,
    })
      .then((res) => {
        articles.value = res.data;
      })
      .catch((err) => console.log(err));
  };

  const createArticle = function (payload) {
    const { title, content, token } = payload;
    axios({
      method: "post",
      url: `${API_URL}/api/articles/create/`,
      data: { title, content },
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => {
        router.push({ name: "community-list" });
      })
      .catch((err) => console.log(err));
  };

  const updateArticle = function (payload) {
    const { title, content, article_id, token } = payload;
    axios({
      method: "put",
      url: `${API_URL}/api/articles/${article_id}/`,
      headers: {
        Authorization: `Token ${token}`,
      },
      data: {
        title,
        content,
      },
    })
      .then((res) => {
        axios({
          method: "get",
          url: `${API_URL}/api/articles/${article_id}/`,
          headers: {
            Authorization: `Token ${token}`,
          },
        })
          .then((res) => {
            router.push({
              name: "community-detail",
              params: { article_id: article_id },
            });
          })
          .catch((err) => console.log(err));
      })
      .catch((err) => console.log(err));
  };

  const deleteArticle = function (id, token) {
    axios({
      method: "delete",
      url: `${API_URL}/api/articles/${id}/`,
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => {
        router.push({ name: "community" });
      })
      .catch((err) => console.log(err));
  };

  const createComment = function (id, token, content) {
    // console.log(id, token, content);
    axios({
      method: "post",
      url: `${API_URL}/api/articles/${id}/comments/`,
      headers: {
        Authorization: `Token ${token}`,
      },
      data: {
        content: content,
      },
    })
      .then((res) => {
        // console.log(res.data);
      })
      .catch((err) => console.log(err));
  };
  const deleteComment = function (payload) {
    const { article_id, comment_id, token } = payload;
    axios({
      method: "delete",
      url: `${API_URL}/api/articles/${article_id}/comments/${comment_id}/`,
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => {
        // console.log(res.data);
      })
      .catch((err) => console.log(err));
  };
  const updateComment = function (payload) {
    const { article_id, comment_id, token, content } = payload;
    axios({
      method: "put",
      url: `${API_URL}/api/articles/${article_id}/comments/${comment_id}/`,
      headers: {
        Authorization: `Token ${token}`,
      },
      data: {
        content: content,
      },
    })
      .then((res) => {
        // console.log(res.data);
      })
      .catch((err) => console.log(err));
  };
  return {
    API_URL,
    articles,
    getArticles,
    createArticle,
    updateArticle,
    deleteArticle,
    updateLike,
    createComment,
    deleteComment,
    updateComment,
  };
});
