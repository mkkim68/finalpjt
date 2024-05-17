<template>
  <div>
    <h3>Savings List</h3>
    {{ store.savings }}
  </div>
</template>

<script setup>
import { useProductStore } from "@/stores/product";
import { onMounted } from "vue";
const store = useProductStore();

onMounted(() => {
  store.getSavings();
});
</script>
