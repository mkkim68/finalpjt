import { defineStore } from 'pinia';
import axios from 'axios';

export const useExchangeStore = defineStore('exchange', {
  state: () => ({
    exchanges: [],
  }),
  actions: {
    async getExchange() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/banks/exchange/');
        this.exchanges = response.data;
      } catch (error) {
        console.error('Failed to fetch exchange rates from API. Using local data.', error);
        await this.getLocalExchange(); // 로컬 데이터로 대체
      }
    },
    async getLocalExchange() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/banks/local/exchange/');
        this.exchanges = [response.data]; // 최신 데이터 하나만 가져옴
      } catch (error) {
        console.error('Failed to fetch local exchange rates', error);
      }
    }
  }
});
