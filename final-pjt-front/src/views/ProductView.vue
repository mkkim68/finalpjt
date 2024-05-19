<template>
  <div class="container">
    <h1>상품 조회</h1>
    <RouterLink to="/product/deposit" active-class="active"> 예금 </RouterLink> |
    <RouterLink to="/product/savings" active-class="active"> 적금 </RouterLink>
    <router-view></router-view>
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

a {
  color: grey;
  font-weight: normal;
  text-decoration: none;
}

.active {
  font-weight: bold;
  color: #4caf50;
}
</style>
