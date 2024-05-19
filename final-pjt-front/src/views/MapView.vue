<template>
  <div class="container">
    <h1>은행 찾기</h1>
    <div class="main">
      <div class="search-panel">
        <form action="#">
          <div class="form-group">
            <label for="bank">은행/도시</label>
            <select id="bank">
              <option value="">서울특별시</option>
              <option value="">부산광역시</option>
            </select>
          </div>
          <div class="form-group">
            <label for="category">시/군/구</label>
            <select id="category">
              <option value="">강남구</option>
              <option value="">서초구</option>
            </select>
          </div>
          <div class="form-group">
            <label for="type">종류</label>
            <select id="type">
              <option value="">국민은행</option>
              <option value="">기업은행</option>
              <option value="">신한은행</option>
              <option value="">우리은행</option>
              <option value="">하나은행</option>
            </select>
          </div>
          <button type="submit">찾기</button>
        </form>
      </div>
      <div class="map-container">
        <iframe
          src="https://www.google.com/maps/d/embed?mid=..."
          width="640"
          height="450"
        ></iframe>
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
  display: flex;
  flex-direction: column;
}

.main {
  display: flex;
  width: 100%;
  justify-content: space-between;
  background-color: #f2f2f2;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-top: 20px;
}

.search-panel {
  width: 30%;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.map-container {
  width: 65%;
  height: 450px;
  border: 1px solid #ddd;
}

.form-group {
  margin-bottom: 10px;
}

label {
  display: block;
  margin-bottom: 5px;
}

select {
  padding-right: 2em; /* 동작 안함*/
  cursor: pointer;
}

select,
button {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}
</style>
