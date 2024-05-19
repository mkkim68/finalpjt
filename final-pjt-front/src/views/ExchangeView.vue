<template>
  <div class="container">
    <h1>환율 계산기</h1>
    <div class="currency-converter">
      <select>
        <option>달러</option>
        <option>유로</option>
        <option>엔</option>
        <option>페소</option>
      </select>
      <input type="text" placeholder="숫자를 입력하세요" />
      <p>* 엔화, 인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
      <div class="buttons">
        <input type="submit" value="확인" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useProductStore } from "@/stores/product";
import { RouterLink } from "vue-router";

const store = useProductStore();

onMounted(() => {});
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

select {
  width: 100px;
  cursor: pointer;
}

input {
  width: 200px;
}

select,
input[type="text"] {
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

div.buttons {
	display: flex;
  flex-direction: column;
	align-items: center;
  padding : 0 50px 0 0;
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
