<template>
  <div class="container">
    <h1>Chart Page</h1>
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
  margin: auto;
  display: flex;
  flex-direction: column;
}
</style>
