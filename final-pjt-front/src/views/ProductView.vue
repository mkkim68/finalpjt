<template>
  <div class="container">
    <h1>상품 조회</h1>
    <RouterLink :to="{ name: 'DepositList' }"> [예금] </RouterLink>
    <RouterLink :to="{ name: 'SavingsList' }"> [적금] </RouterLink>
  </div>
  <DepositList />
  <SavingsList />
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useProductStore } from "@/stores/product";
import { RouterLink } from "vue-router";
import DepositList from "@/components/DepositList.vue";
import SavingsList from "@/components/SavingsList.vue";

const store = useProductStore();

onMounted(() => {});
</script>

<style scoped>
.container {
  width: 90%;
  margin: auto;
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
  max-width: 30%;
}

.table-section {
  flex: 2;
}
</style>
