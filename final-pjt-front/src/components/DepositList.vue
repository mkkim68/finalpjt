<template>
  <div class="container">
    <div class="filter-section">
      <h4>검색하기</h4>
      <p>검색 조건을 입력하세요.</p>
      <hr />
      <form action="">
        <div class="condition">
          <p>은행</p>
          <select name="bank" id="bank">
            <option value="국민">국민</option>
            <option value="신한">신한</option>
            <option value="우리">우리</option>
            <option value="하나">하나</option>
          </select>
        </div>
        <div class="condition">
          <p>예치기간</p>
          <select name="duration" id="duration">
            <optgroup label="단기">
              <option value="1">1</option>
              <option value="2">2</option>
            </optgroup>
            <optgroup label="중기">
              <option value="3">3</option>
              <option value="4">4</option>
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
        <tr>
          <th class="first">금융회사명</th>
          <th class="second">상품명</th>
          <th class="third">이자율</th>
        </tr>
        <tr v-for="deposit in deposits" :key="deposit.id">
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <td>{{ deposit.mtrt_int }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from "vue";
import { useProductStore } from "@/stores/product";

const store = useProductStore();
onMounted(() => {
  store.getDeposits();
});

const deposits = computed(() => store.deposits);
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
  margin-top: 2px;
  padding: 20px;
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
  height: 30px;
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
