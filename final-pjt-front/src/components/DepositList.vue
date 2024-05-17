<template>
  <div>
    <div class="search">
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
    <div class="result">
      <h3>정기 예금</h3>
      <ul>
        <li v-for="deposit in deposits" :key="deposit.id">
          {{ deposit.kor_co_nm }} - {{ deposit.fin_prdt_nm }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { useProductStore } from "@/stores/product";
import { onMounted, computed } from "vue";
const store = useProductStore();

onMounted(() => {
  store.getDeposits();
});

const deposits = computed(() => store.deposits);
</script>
