<template>
  <div class="container2">
    <div class="filter-section">
      <form @submit.prevent="savingFilter">
        <p>검색 조건을 입력하세요.</p>
        <hr />
        <div class="condition">
          <label for="bank">은행</label>
          <br />
          <select name="bank" id="bank" v-model="bank">
            <option disabled value="null">은행을 선택해주세요</option>
            <option value="all">전체</option>
            <option value="우리은행">우리은행</option>
            <option value="국민은행">국민은행</option>
            <option value="신한은행">신한은행</option>
            <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
            <option value="한국씨티은행">한국씨티은행</option>
            <option value="하나은행">하나은행</option>
            <option value="농협은행주식회사">농협은행주식회사</option>
            <option value="카카오뱅크">카카오뱅크</option>
            <option value="토스뱅크">토스뱅크</option>
            <option value="대구은행">대구은행</option>
            <option value="부산은행">부산은행</option>
            <option value="광주은행">광주은행</option>
            <option value="제주은행">제주은행</option>
            <option value="수협은행">수협은행</option>
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
      <h3>정기 적금</h3>
      <table>
        <thead style="text-align: center;">
          <tr>
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
          <tr v-for="saving in filteredSavings" :key="saving.id">
            <td>{{ saving.kor_co_nm }}</td>
            <td>{{ saving.fin_prdt_nm }}</td>
            <td>{{ getInterestRate(saving, 6) }}</td>
            <td>{{ getInterestRate(saving, 12) }}</td>
            <td>{{ getInterestRate(saving, 24) }}</td>
            <td>{{ getInterestRate(saving, 36) }}</td>
          </tr>
        </tbody>
      </table>

    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useProductStore } from "@/stores/product";

const bank = ref("all");
const duration = ref("all");
const filteredSavings = ref([]);

const store = useProductStore();
onMounted(async () => {
  await store.getSavings();
  savingFilter();
});

const savings = computed(() => store.savings);

const savingFilter = () => {
  let filtered = savings.value;

  if (bank.value !== 'all') {
    filtered = filtered.filter(saving => saving.kor_co_nm === bank.value);
  }

  if (duration.value !== 'all') {
    const durationNum = Number(duration.value);
    filtered = filtered.map(saving => {
      const filteredOptions = saving.options.filter(option => Number(option.save_trm) === durationNum);
      return { ...saving, options: filteredOptions };
    }).filter(saving => saving.options.length > 0);
  } else {
    filtered = filtered.map(saving => {
      const filteredOptions = saving.options.filter(option => [6, 12, 24, 36].includes(Number(option.save_trm)));
      return { ...saving, options: filteredOptions };
    });
  }

  filteredSavings.value = filtered;
};

const getInterestRate = (saving, term) => {
  const option = saving.options.find(option => Number(option.save_trm) === term);
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

th.first {
  width: 18%;
}

th.second {
  width: 32%;
}

th.third {
  width: 20%;
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
