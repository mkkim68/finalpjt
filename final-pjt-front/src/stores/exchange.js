import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import axios from "axios";

export const useExchangeStore = defineStore('exchange', () => {
  const exchanges = ref([]);
  const API_URL = 'http://127.0.0.1:8000';

  const getExchange = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/bank/exchange/`);
      exchanges.value = response.data;
    } catch (error) {
      console.error('Failed to fetch exchange rates:', error);
    }
  };

  return { exchanges, getExchange };
});
