import { defineStore } from 'pinia';
import axios from 'axios';

export const useExchangeStore = defineStore('exchange', {
  state: () => ({
    exchanges: [],
  }),
  actions: {
    async getExchange() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/bank/exchange/');
        this.exchanges = response.data;
      } catch (error) {
        throw new Error('Failed to fetch exchange rates');
      }
    },
    async getLocalExchange() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/local/exchange/');
        this.exchanges = [response.data]; // 최신 데이터 하나만 가져옴
      } catch (error) {
        console.error('Failed to fetch local exchange rates', error);
      }
    }
  }
});
