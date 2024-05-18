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
import { onMounted } from "vue";
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
</style>
