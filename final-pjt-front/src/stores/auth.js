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
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          email: payload.email,
          password1: payload.password1,
          password2: payload.password2,
          age: payload.age,
          balance: payload.balance,
          income: payload.income,
          favorite_bank: payload.favorite_bank,
          invest_type: payload.invest_type,
        },
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
      return token.value !== null;
    });

    const userUpdate = function (payload) {
      const {
        username,
        email,
        age,
        balance,
        income,
        favorite_bank,
        invest_type,
        user_id,
      } = payload;
      axios({
        method: "put",
        url: `${API_URL}/accounts/${user_id}/update/`,
        data: {
          username,
          email,
          age,
          balance,
          income,
          favorite_bank,
          invest_type,
        },
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          router.push({ name: "ProfileView", params: { user_id: user_id } });
        })
        .catch((err) => console.log(err));
    };

    const getUserInfo = function (user_id) {
      axios({
        method: "get",
        url: `${API_URL}/accounts/${user_id}/`,
      })
        .then((res) => {
          info.value = res.data;
        })
        .catch((err) => console.log(err));
    };

    return {
      API_URL,
      signUp,
      logIn,
      token,
      isLogin,
      logOut,
      info,
      userUpdate,
      getUserInfo,
    };
  },
  { persist: true }
);
