import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import axios from "axios";

export const useProductStore = defineStore(
  "product",
  () => {
    const deposits = ref([]);
    const savings = ref([]);
    const API_URL = "http://127.0.0.1:8000";
    const token = ref(null);

    const getDeposits = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/bank/deposits/`,
        // headers: {
        //   Authorization: `Token ${token.value}`,
        // },
      })
        .then((response) => {
          deposits.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const getSavings = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/bank/savings/`,
        // headers: {
        //   Authorization: `Token ${token.value}`,
        // },
      })
        .then((response) => {
          savings.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    return { deposits, savings, API_URL, getDeposits, getSavings };
  },
  { persist: true }
);
