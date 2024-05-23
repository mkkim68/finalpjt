import { ref } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useProductStore = defineStore(
  "product",
  () => {
    const deposits = ref([]);
    const savings = ref([]);
    const banks = {
      "0010001": "우리은행",
      "0010927": "국민은행",
      "0011625": "신한은행",
      "0010002": "한국스탠다드차타드은행",
      "0010006": "한국씨티은행",
      "0013909": "하나은행",
      "0013175": "농협",
      "0015130": "카카오뱅크",
      "0017801": "토스뱅크",
      "0010016": "대구은행",
      "0010017": "부산은행",
      "0010019": "광주은행",
      "0010020": "제주은행",
      "0014807": "수협은행",
    };
    const loadingDeposits = ref(false);
    const loadingSavings = ref(false);
    const API_URL = "http://127.0.0.1:8000";

    const getDeposits = async () => {
      deposits.value = []; // 초기화
      loadingDeposits.value = true; // 로딩 상태 시작
      try {
        const depositResponse = await axios.get(
          `${API_URL}/api/banks/deposits/`
        );
        const depositOptionsResponse = await axios.get(
          `${API_URL}/api/banks/deposit-options/`
        );

        for (const deposit of depositResponse.data) {
          const options = depositOptionsResponse.data.filter(
            (item) => item.fin_prdt_cd === deposit.fin_prdt_cd
          );
          deposits.value.push({ ...deposit, options });
        }
      } catch (error) {
        console.error(error);
      } finally {
        loadingDeposits.value = false; // 로딩 상태 종료
      }
    };

    const getSavings = async () => {
      savings.value = []; // 초기화
      loadingSavings.value = true; // 로딩 상태 시작
      try {
        const savingResponse = await axios.get(`${API_URL}/api/banks/savings/`);
        const savingOptionsResponse = await axios.get(
          `${API_URL}/api/banks/saving-options/`
        );

        for (const saving of savingResponse.data) {
          const options = savingOptionsResponse.data.filter(
            (item) => item.fin_prdt_cd === saving.fin_prdt_cd
          );
          savings.value.push({ ...saving, options });
        }
      } catch (error) {
        console.error(error);
      } finally {
        loadingSavings.value = false; // 로딩 상태 종료
      }
    };
    const joinDeposit = function (payload) {
      const { fin_prdt_cd, token } = payload;
      axios({
        method: "post",
        url: `${API_URL}/api/banks/deposits/${fin_prdt_cd}/join/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((res) => {})
        .catch((err) => console.log(err));
    };
    const joinSaving = function (payload) {
      const { fin_prdt_cd, token } = payload;
      axios({
        method: "post",
        url: `${API_URL}/api/banks/savings/${fin_prdt_cd}/join/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((res) => {})
        .catch((err) => console.log(err));
    };

    return {
      deposits,
      savings,
      banks,
      loadingDeposits,
      loadingSavings,
      getDeposits,
      getSavings,
      joinDeposit,
      joinSaving,
    };
  },
  { persist: true }
);
