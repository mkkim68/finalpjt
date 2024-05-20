import { ref } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useProductStore = defineStore("product", () => {
  const deposits = ref([]);
  const savings = ref([]);
  const loadingDeposits = ref(false);
  const loadingSavings = ref(false);
  const API_URL = "http://127.0.0.1:8000";

  const getDeposits = async () => {
    deposits.value = []; // 초기화
    loadingDeposits.value = true; // 로딩 상태 시작
    try {
      const depositResponse = await axios.get(`${API_URL}/api/banks/deposits/`);
      const depositOptionsResponse = await axios.get(`${API_URL}/api/banks/deposit-options/`);
      
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
      const savingOptionsResponse = await axios.get(`${API_URL}/api/banks/saving-options/`);
      
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

  return { deposits, savings, loadingDeposits, loadingSavings, getDeposits, getSavings };
}, { persist: true });
