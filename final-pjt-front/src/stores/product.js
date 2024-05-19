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
          axios({
            method: "get",
            url: `${API_URL}/api/bank/deposit-options/`,
          })
            .then((res) => {
              console.log(res.data);
              for (const deposit of response.data) {
                const option = res.data.filter(
                  (item) => item.fin_prdt_cd === deposit.fin_prdt_cd
                );
                deposits.value.push({ ...deposit, options: option });
              }
            })
            .catch((err) => console.log(err));
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
          axios({
            method: "get",
            url: `${API_URL}/api/bank/saving-options/`,
          })
            .then((res) => {
              console.log(res.data);
              for (const saving of response.data) {
                const option = res.data.filter(
                  (item) => item.fin_prdt_cd === saving.fin_prdt_cd
                );
                savings.value.push({ ...saving, options: option });
              }
            })
            .catch((err) => console.log(err));
        })
        .catch((error) => {
          console.log(error);
        });
    };

    return { deposits, savings, API_URL, getDeposits, getSavings };
  },
  { persist: true }
);
