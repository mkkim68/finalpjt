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
        </div>
        <div class="input-row">
          <input type="text" v-model="amountInCurrency" placeholder="숫자를 입력하세요" @input="calculateToKRW" />
          <button disabled>{{ selectedCurrency }}</button>
        </div>
        <div class="arrow">
          <img class="icon" src="@/assets/exchange_arrow.png" alt="arrow">
        </div>
        <div class="results">
          <input type="text" v-model="amountInKRW" placeholder="환전 결과" @input="calculateToCurrency" />
          <button disabled>₩</button>
        </div>
      </div>
      <p>* 엔화, 인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
    </div>

    <div class="currency-table">
      <table>
        <thead style="text-align: center">
          <tr>
            <th class="first">통화코드</th>
            <th class="second">국가/통화명</th>
            <th class="third">송금 받을 때 </th>
            <th class="third">송금 보낼 때</th>
            <th class="third">매매 기준율</th>
            <th class="third">장부 가격</th>
            <th class="third">서울외국환중개 매매기준율</th>
            <th class="third">서울외국환중개 장부가격</th>
          </tr>
        </thead>
        <tbody style="text-align: right">
          <tr v-for="exchange in exchanges" :key="exchange.id">
            <td style="text-align: left">{{ exchange.cur_unit }}</td>
            <td style="text-align: left">{{ exchange.cur_nm }}</td>
            <td>{{ exchange.ttb }}</td>
            <td>{{ exchange.tts }}</td>
            <td>{{ exchange.deal_bas_r }}</td>
            <td>{{ exchange.bkpr }}</td>
            <td>{{ exchange.kftc_deal_bas_r }}</td>
            <td>{{ exchange.kftc_bkpr }}</td>
          </tr>
        </tbody>
      </table>
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
  try {
    await store.getExchange();
  } catch (error) {
    console.error('Failed to fetch exchange rates from API. Using local data.', error);
    await store.getLocalExchange(); // 로컬 데이터베이스에서 데이터 가져오기
  }
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
  flex-wrap: wrap;
  align-items: center;
}

.request, .input-row, .results, .arrow {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
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
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 5px;
}

.icon {
  width: 20px;
}

p {
  margin-top: 10px;
}

.currency-table {
  width: 100%;
  margin: 50px 0;
}

table {
  width: 100%;
  border: 1px solid black;
  border-collapse: collapse;
  background-color: #fafafa;
}

thead {
  background-color: #f4fff4;
}

th,
td {
  border: 1px solid #ccc;
  padding: 10px;
  font-size: 1em;
}

th.first {
  width: 10%;
}

th.second {
  width: 23%;
}

th.third {
  width: 10%;
}

@media (max-width: 992px) {
  .input-group {
    flex-direction: column;
    align-items: flex-start;
  }

  .request, .input-row, .results {
    width: 100%;
    justify-content: flex-start;
  }

  .arrow {
    width: 100%;
    display: flex;
    justify-content: center; /* 중앙 정렬 */
    margin-bottom: 15px;
  }

  .input-row, .results {
    flex-direction: row;
    width: 100%;
  }

  select, input[type="text"], button {
    width: calc(50% - 5px);
    margin-right: 5px;
    margin-bottom: 10px;
  }

  input[type="text"], button {
    margin-left: 5px;
  }
}
</style>