<template>
  <div class="container">
    <div class="filter-section">
      <form @submit.prevent="depositFilter(bank, duration)">
        <p>검색 조건을 입력하세요.</p>
        <hr />
        <label for="bank">은행을 선택하세요</label>
        <br />
        <select name="bank" id="bank" v-model="bank">
          <option disabled>은행을 선택해주세요</option>
          <option value="all">전체</option>
          <option value="0010001">우리은행</option>
          <option value="0010927">국민은행</option>
          <option value="0011625">신한은행</option>
          <option value="0010002">한국스탠다드차타드은행</option>
          <option value="0010006">한국씨티은행</option>
          <option value="0013909">하나은행</option>
          <option value="0013175">농협은행주식회사</option>
          <option value="0015130">카카오뱅크</option>
          <option value="0017801">토스뱅크</option>
          <option value="0010016">대구은행</option>
          <option value="0010017">부산은행</option>
          <option value="0010019">광주은행</option>
          <option value="0010020">제주은행</option>
          <option value="0014807">수협은행</option></select
        ><br />
        <label for="duration">예치기간</label><br />
        <select name="duration" id="duration" v-model="duration">
          <option disabled>기간을 선택해주세요</option>
          <option value="all">전체기간</option>
          <optgroup label="단기">
            <option value="1">1년 미만</option>
            <option value="2">1년 이상 2년 미만</option>
          </optgroup>
          <optgroup label="중기">
            <option value="3">2년 이상 3년 미만</option>
            <option value="4">3년 이상</option>
          </optgroup>
        </select>
        <hr />
        <input type="submit" value="확인" />
      </form>
    </div>
    <div class="table-section">
      <h3>정기 적금</h3>
      <ul>
        <li v-for="saving in savings" :key="saving.id">
          <span>{{ saving.kor_co_nm }}</span> -
          <span>{{ saving.fin_prdt_nm }}</span>
          <div>
            <h4>옵션</h4>
            <div v-for="option in saving.options">
              <span
                >{{ option.intr_rate_type_nm }}/저축 금리:
                {{ option.intr_rate }}/최고 우대 금리:
                {{ option.intr_rate2 }}/저축 기간: {{ option.save_trm }}</span
              >
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from "vue";
import { useProductStore } from "@/stores/product";

const store = useProductStore();
onMounted(() => {
  store.getSavings();
});

const savings = computed(() => store.savings);
</script>

<style scoped>
.container {
  display: flex;
  gap: 20px;
  width: 95%;
  margin: 0 auto;
}

.filter-section,
.table-section {
  margin-top: 20px;
  padding: 0 20px;
  background-color: #f4f4f4;
  border: 1px solid #ddd;
}

.filter-section {
  flex: 1;
  max-width: 18%;
}

div.condition {
  margin: 20px 10px;
}

form > div > select {
  width: 50%;
  height: 25px;
  padding: 1px 0px;
  cursor: pointer;
}

form > div > p {
  font-size: 0.85em;
  margin: 5px 0px;
}

.table-section {
  flex: 2;
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

th.first {
  width: 18%;
}

th.second {
  width: 30%
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
