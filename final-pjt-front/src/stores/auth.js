import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const token = ref(null);
    const API_URL = "http://127.0.0.1:8000";
    const router = useRouter();

    const signUp = function (payload) {
      const {
        username,
        password1,
        password2,
        age,
        balance,
        income,
        favorite_bank,
        invest_type,
      } = payload;

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          console.log("회원가입이 완료되었습니다.");
          // 회원가입 성공 후 자동으로 로그인까지 진행하기
          const password = password1;
          logIn({ username, password });
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
          console.log("로그인이 완료되었습니다.");
          console.log(res.data);
          token.value = res.data.key;
          router.push({ name: "ProductView" });
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

    return { API_URL, signUp, logIn, token, isLogin };
  },
  { persist: true }
);
