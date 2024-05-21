<template>
  <div class="container">
    <h1>Chart Page</h1>
    <form @submit.prevent="print">
      <input type="submit" value="내 차트 출력하기" />
    </form>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useProductStore } from "@/stores/product";
import { useChartStore } from "@/stores/chart";
import { RouterLink } from "vue-router";

const chartStore = useChartStore();
const temp = ref(null);

const print = function () {
  chartStore.printChart();
};

onMounted(() => {});
</script>

<style scoped>
.container {
  width: 90%;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
}
</style>
