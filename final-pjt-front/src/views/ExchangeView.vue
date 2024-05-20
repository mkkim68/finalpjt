<template>
  <div class="container">
    <h1>환율 계산기</h1>
    <div class="currency-converter">
      <div class="input-group">
        <div class="request">
          <select v-model="selectedCurrency">
            <option v-for="exchange in exchanges" :key="exchange.cur_unit" :value="exchange.cur_unit">
              {{ exchange.cur_nm }}
            </option>
          </select>
          <input type="text" v-model="amountInCurrency" placeholder="숫자를 입력하세요" @input="calculateToKRW" />
          <button disabled>{{ selectedCurrency }}</button>
        </div>
        <div class="results">
          <img class="icon arrow" src="@/assets/exchange_arrow.png" alt="arrow">
          <input type="text" v-model="amountInKRW" placeholder="환전 결과" @input="calculateToCurrency" />
          <button disabled>₩</button>
        </div>
      </div>
      <p>* 엔화, 인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useExchangeStore } from "@/stores/exchange";

const store = useExchangeStore();
const exchanges = computed(() => store.exchanges);
const selectedCurrency = ref('USD');
const amountInCurrency = ref('');
const amountInKRW = ref('');

const calculateToKRW = () => {
  if (selectedCurrency.value && amountInCurrency.value) {
    const exchange = exchanges.value.find(exchange => exchange.cur_unit === selectedCurrency.value);
    if (exchange) {
      const exchangeRate = exchange.deal_bas_r;
      amountInKRW.value = (amountInCurrency.value * exchangeRate).toFixed(2);
    } else {
      amountInKRW.value = '올바른 값을 입력하세요.';
    }
  } else {
    amountInKRW.value = '';
  }
};

const calculateToCurrency = () => {
  if (selectedCurrency.value && amountInKRW.value) {
    const exchange = exchanges.value.find(exchange => exchange.cur_unit === selectedCurrency.value);
    if (exchange) {
      const exchangeRate = exchange.deal_bas_r;
      amountInCurrency.value = (amountInKRW.value / exchangeRate).toFixed(2);
    } else {
      amountInCurrency.value = '올바른 값을 입력하세요.';
    }
  } else {
    amountInCurrency.value = '';
  }
};

onMounted(async () => {
  await store.getExchange();
  calculateToKRW(); // 데이터가 로드된 후 계산 함수 호출
  console.log("Exchanges: ", exchanges.value); // 데이터를 콘솔에 출력하여 확인
});

watch([selectedCurrency], () => {
  calculateToKRW();
  calculateToCurrency();
});
</script>

<style scoped>
.container {
  width: 90%;
  margin: 20px auto;
}

.currency-converter {
  background-color: #f2f2f2;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-top: 20px;
}

.input-group {
  display: flex;
  align-items: center;
}

select, input[type="text"], button {
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4caf50;
  color: white;
  border: none;
  cursor: pointer;
}

input[type="text"][readonly] {
  background-color: #e9ecef;
}

.arrow {
  width: 40px;
  margin: 0px 20px;
}

.request, .result {
  display: flex;
  align-items: center;
}


p {
  margin-top: 10px;
}
</style>
