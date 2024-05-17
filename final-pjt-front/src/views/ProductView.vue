<template>
  <div class="container">
    <h1>Product Page</h1>
    <RouterLink :to="{ name: 'DepositList' }"> [예금] </RouterLink>
    <RouterLink :to="{ name: 'SavingsList' }"> [적금] </RouterLink>
    <DepositList />
    <SavingsList />
  </div>
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
  margin-left: 30px;
}
</style>
