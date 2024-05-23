<template>
  <div class="container">
    <h1 v-if="!product">{{ authStore.info.username }}님에게 딱 맞는 예금</h1>
    <h1 v-else>{{ authStore.info.username }}님에게 딱 맞는 적금</h1>
    <form>
      <div class="form-check form-switch">
        <input
          class="form-check-input"
          type="checkbox"
          role="switch"
          id="flexSwitchCheckChecked"
          v-model="product"
        />
        <label class="form-check-label" for="flexSwitchCheckChecked"
          >예금/적금</label
        >
      </div>
      <div class="search-btns">
        <input
          type="checkbox"
          class="btn-check"
          id="age"
          autocomplete="off"
          v-model="age"
        />
        <label class="btn btn-outline-success" for="age">연령별</label>
        <input
          type="checkbox"
          class="btn-check"
          id="income"
          autocomplete="off"
          v-model="income"
        />
        <label class="btn btn-outline-success" for="income">수입</label>
        <input
          type="checkbox"
          class="btn-check"
          id="balance"
          autocomplete="off"
          v-model="balance"
        />
        <label class="btn btn-outline-success" for="balance">재산</label>
        <input
          type="checkbox"
          class="btn-check"
          id="favorite_bank"
          autocomplete="off"
          v-model="favorite_bank"
        />
        <label class="btn btn-outline-success" for="favorite_bank"
          >주거래은행</label
        >
        <input
          type="checkbox"
          class="btn-check"
          id="invest_type"
          autocomplete="off"
          v-model="invest_type"
        />
        <label class="btn btn-outline-success" for="invest_type"
          >저축 성향</label
        >
      </div>
    </form>
  </div>
  <DepositRecommend
    v-if="!product"
    :age="age"
    :income="income"
    :balance="balance"
    :invest_type="invest_type"
    :favorite_bank="favorite_bank"
  />
  <SavingRecommend
    v-else
    :age="age"
    :income="income"
    :balance="balance"
    :invest_type="invest_type"
    :favorite_bank="favorite_bank"
  />
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useChartStore } from "@/stores/chart";
import { useAuthStore } from "@/stores/auth";
import { useProductStore } from "@/stores/product";
import { RouterLink, RouterView } from "vue-router";
import SavingRecommend from "@/components/SavingRecommend.vue";
import DepositRecommend from "@/components/DepositRecommend.vue";

const chartStore = useChartStore();
const authStore = useAuthStore();
const productStore = useProductStore();

const product = ref(false);
const age = ref(null);
const income = ref(null);
const balance = ref(null);
const favorite_bank = ref(null);
const invest_type = ref(null);

onMounted(() => {});
</script>

<style scoped>
.search-btns > label {
  margin-right: 10px !important;
}
.container {
  width: 90%;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
}
</style>
