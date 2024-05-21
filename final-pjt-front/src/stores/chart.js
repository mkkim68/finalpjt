import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import axios from "axios";

export const useChartStore = defineStore("chart", () => {
  const printChart = function () {
    print();
  };
  return { printChart };
});
