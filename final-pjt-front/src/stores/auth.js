import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const token = ref(null);
    const info = ref([]);
    const API_URL = "http://127.0.0.1:8000";
    const router = useRouter();

    const signUp = function (payload) {
      const data = ref({});
      for (const item in payload) {
        if (payload[item] !== null) {
          data.value[item] = payload[item];
        }
      }
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: data.value,
      })
        .then((res) => {
          router.push({ name: "LogInView" });
        })
        .catch((err) => console.log(err));
    };

    const logIn = function (payload) {
      const { username, password } = payload;

      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          token.value = res.data.key;
          router.push({ name: "HomeView" });
          axios({
            method: "get",
            url: `${API_URL}/accounts/${username}/`,
          })
            .then((res) => {
              info.value = res.data;
            })
            .catch((err) => console.log(err));
        })
        .catch((err) => console.log(err));
    };

    const logOut = function () {
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
      })
        .then((res) => {
          router.push({ name: "LogInView" });
          token.value = null;
          info.value = null;
        })
        .catch((err) => console.log(err));
    };

    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    return { API_URL, signUp, logIn, token, isLogin, logOut, info };
  },
  { persist: true }
);
