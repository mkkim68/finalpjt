<template>
  <div>
    <div class="bank-container">
      <div class="filter-section">
        <h4>검색하기</h4>
        <p>검색 조건을 입력하세요.</p>
        <hr />
        <form action="">
          <p>은행을 선택하세요</p>
          <select name="bank" id="bank">
            <option value="국민">국민</option>
            <option value="신한">신한</option>
            <option value="우리">우리</option>
            <option value="하나">하나</option>
          </select>
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
          <hr />
          <input type="submit" value="확인" />
        </form>
      </div>
      <div class="table-section">
        <h3>정기 적금</h3>
        <ul>
          <li>리스트</li>
        </ul>
      </div>
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

const savings = computed(() => store.products);
</script>

<style scoped>
.bank-container {
  display: flex;
  gap: 20px;
  width: 95%;
  margin: 0 auto;
}

.filter-section,
.table-section {
  margin-top: 20px;
  padding: 10px;
  background-color: #f4f4f4;
  border: 1px solid #ddd;
}

.filter-section {
  flex: 1;
  max-width: 30%;
}

.table-section {
  flex: 2;
}
</style>
