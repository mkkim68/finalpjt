<template>
  <div class="container2">
    <div class="filter-section">
      <form @submit.prevent="depositFilter()">
        <p>검색 조건을 입력하세요.</p>
        <hr />
        <div class="condition">
          <label for="bank">은행</label>
          <br />
          <select name="bank" id="bank" v-model="bank">
            <option disabled value="null">은행을 선택해주세요</option>
            <option value="all">전체</option>
            <option v-for="name in sortedBankNames" :key="name" :value="name">{{ name }}</option>
          </select><br />
        </div>
        <div class="condition">
          <label for="duration">예치기간</label><br />
          <select name="duration" id="duration" v-model="duration">
            <option disabled value="null">기간을 선택해주세요</option>
            <option value="all">전체기간</option>
            <optgroup label="단기">
              <option value="6">1년 미만</option>
              <option value="12">1년 이상 2년 미만</option>
            </optgroup>
            <optgroup label="중기">
              <option value="24">2년 이상 3년 미만</option>
              <option value="36">3년 이상</option>
            </optgroup>
          </select>
        </div>
        <hr />
        <div class="buttons">
          <input type="submit" value="확인" />
        </div>
      </form>
    </div>
    <div class="table-section">
      <h3>정기 예금</h3>
      <table>
        <thead style="text-align: center;">
          <tr>
            <th class="plus" rowspan="2">금융상품 코드</th>
            <th class="first" rowspan="2">은행명</th>
            <th class="second" rowspan="2">상품명</th>
            <th class="third" colspan="4">금리</th>
          </tr>
          <tr>
            <th>6개월</th>
            <th>12개월</th>
            <th>24개월</th>
            <th>36개월</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="deposit in filteredDeposits" :key="deposit.id">
            <td>{{ deposit.fin_prdt_cd }}</td>
            <td>{{ deposit.kor_co_nm }}</td>
            <td>{{ deposit.fin_prdt_nm }}</td>
            <td>{{ getInterestRate(deposit, 6) }}</td>
            <td>{{ getInterestRate(deposit, 12) }}</td>
            <td>{{ getInterestRate(deposit, 24) }}</td>
            <td>{{ getInterestRate(deposit, 36) }}</td>
          </tr>
        </tbody>
      </table>

    </div>
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from "vue";
import { useProductStore } from "@/stores/product";

const bank = ref("all");
const duration = ref("all");
const filteredDeposits = ref([]);
const bankNames = ref([]);

const store = useProductStore();

const extractBankNames = (deposits) => {
  const names = deposits.map(deposit => deposit.kor_co_nm);
  return [...new Set(names)];
};

const sortedBankNames = computed(() => {
  return bankNames.value.sort((a,b) => a.localeCompare(b))
})

onMounted(async () => {
  await store.getDeposits();
  bankNames.value = extractBankNames(store.deposits);
  depositFilter();
});

const deposits = computed(() => store.deposits);

const depositFilter = () => {
  let filtered = deposits.value;

  if (bank.value !== 'all') {
    filtered = filtered.filter(deposit => deposit.kor_co_nm === bank.value);
  }

  if (duration.value !== 'all') {
    const durationNum = Number(duration.value);
    filtered = filtered.map(deposit => {
      const filteredOptions = deposit.options.filter(option => Number(option.save_trm) === durationNum);
      return { ...deposit, options: filteredOptions };
    }).filter(deposit => deposit.options.length > 0);
  } else {
    filtered = filtered.map(deposit => {
      const filteredOptions = deposit.options.filter(option => [6, 12, 24, 36].includes(Number(option.save_trm)));
      return { ...deposit, options: filteredOptions };
    });
  }

  filteredDeposits.value = filtered;
};

const getInterestRate = (deposit, term) => {
  const option = deposit.options.find(option => Number(option.save_trm) === term);
  return option ? option.intr_rate : '-';
};
</script>


<style scoped>
.container2 {
  display: flex;
  gap: 20px;
  width: 100%;
  margin: 0 auto;
}

.filter-section,
.table-section {
  margin-top: 2px;
  padding: 20px;
  background-color: #f4f4f4;
  border: 1px solid #ddd;
}

.filter-section {
  flex: 1;
  max-width: 250px;
}

div.condition {
  margin: 20px 10px;
}

form > div > select {
  width: 100%;
  height: 30px;
  padding: 1px 0px;
  cursor: pointer;
}

.table-section {
  flex: 2;
  width: 100%;
}

table {
  width: 100%;
  border: 1px solid black;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ccc;
  padding: 10px;
  font-size: 0.8em;
}

th.plus {
  width: 14%;
}

th.first {
  width: 16%;
}

th.second {
  width: 25%;
}

th.third {
  width: 22%;
}

div.buttons {
	display: flex;
  flex-direction: column;
	align-items: center;
}

div.buttons > input {
  padding: 10px 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 80px;
  margin-top: 20px;
}

</style>
