<template>
  <div class="container">
    <h1>{{ authStore.info.username }}님에게 딱 맞는 상품</h1>
    <!-- <form @submit.prevent="print">
      <input type="submit" value="내 차트 출력하기" />
    </form> -->
    <div>
      <h2>예금</h2>
      <div v-if="deposits_bank">
        <h3>
          {{ authStore.info.username }}님의 주거래은행
          {{ authStore.info.favorite_bank }}의 상품들
        </h3>
        <p v-for="deposit in deposits_bank" :key="deposit.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'DepositDetail',
              params: { fin_prdt_cd: deposit.fin_prdt_cd },
            }"
            >{{ deposit.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
      <div v-if="deposits_age">
        <h3>{{ authStore.info.username }}님의 또래들은 이 상품을 선택했어요</h3>
        <p v-for="deposit in deposits_age" :key="deposit.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'DepositDetail',
              params: { fin_prdt_cd: deposit.fin_prdt_cd },
            }"
            >{{ deposit.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
      <div v-if="deposits_income">
        <h3>
          {{ authStore.info.username }}님과 수입이 비슷한 사람들은 이 상품을
          선택했어요
        </h3>
        <p v-for="deposit in deposits_income" :key="deposit.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'DepositDetail',
              params: { fin_prdt_cd: deposit.fin_prdt_cd },
            }"
            >{{ deposit.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
      <div v-if="deposits_balance">
        <h3>
          {{ authStore.info.username }}님의 전재산과 비슷한 사람들은 이 상품을
          선택했어요
        </h3>
        <p v-for="deposit in deposits_balance" :key="deposit.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'DepositDetail',
              params: { fin_prdt_cd: deposit.fin_prdt_cd },
            }"
            >{{ deposit.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
      <div v-if="deposits_type">
        <h3>
          {{ authStore.info.username }}님과 같은 저축 성향
          {{ authStore.info.invest_type }}형인 사람들은 이 상품을 선택했어요
        </h3>
        <p v-for="deposit in deposits_type" :key="deposit.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'DepositDetail',
              params: { fin_prdt_cd: deposit.fin_prdt_cd },
            }"
            >{{ deposit.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
    </div>
    <div>
      <h2>적금</h2>
      <div v-if="savings_bank">
        <h3>
          {{ authStore.info.username }}님의 주거래은행
          {{ authStore.info.favorite_bank }}의 상품들
        </h3>
        <p v-for="saving in savings_bank" :key="saving.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'SavingsDetail',
              params: { fin_prdt_cd: saving.fin_prdt_cd },
            }"
            >{{ saving.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
      <div v-if="savings_age">
        <h3>{{ authStore.info.username }}님의 또래들은 이 상품을 선택했어요</h3>
        <p v-for="saving in savings_age" :key="saving.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'SavingsDetail',
              params: { fin_prdt_cd: saving.fin_prdt_cd },
            }"
            >{{ saving.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
      <div v-if="savings_income">
        <h3>
          {{ authStore.info.username }}님과 수입이 비슷한 사람들은 이 상품을
          선택했어요
        </h3>
        <p v-for="saving in savings_income" :key="saving.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'SavingsDetail',
              params: { fin_prdt_cd: saving.fin_prdt_cd },
            }"
            >{{ saving.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
      <div v-if="savings_balance">
        <h3>
          {{ authStore.info.username }}님의 전재산과 비슷한 사람들은 이 상품을
          선택했어요
        </h3>
        <p v-for="saving in savings_balance" :key="saving.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'SavingsDetail',
              params: { fin_prdt_cd: saving.fin_prdt_cd },
            }"
            >{{ saving.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
      <div v-if="savings_type">
        <h3>
          {{ authStore.info.username }}님과 같은 저축 성향
          {{ authStore.info.invest_type }}형인 사람들은 이 상품을 선택했어요
        </h3>
        <p v-for="saving in savings_type" :key="saving.fin_prdt_cd">
          <RouterLink
            :to="{
              name: 'SavingsDetail',
              params: { fin_prdt_cd: saving.fin_prdt_cd },
            }"
            >{{ saving.fin_prdt_nm }}</RouterLink
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useChartStore } from "@/stores/chart";
import { useAuthStore } from "@/stores/auth";
import { RouterLink } from "vue-router";
import axios from "axios";

const chartStore = useChartStore();
const authStore = useAuthStore();
const API_URL = "http://127.0.0.1:8000";

const print = function () {
  chartStore.printChart();
};

const deposits_age = ref(null);
const deposits_balance = ref(null);
const deposits_bank = ref(null);
const deposits_income = ref(null);
const deposits_type = ref(null);
const savings_age = ref(null);
const savings_balance = ref(null);
const savings_bank = ref(null);
const savings_income = ref(null);
const savings_type = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: `${API_URL}/api/banks/recommend/${authStore.info.id}/`,
    headers: {
      Authorization: `Token ${authStore.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      deposits_age.value = res.data.deposit["age"];
      deposits_balance.value = res.data.deposit["balance"];
      deposits_bank.value = res.data.deposit["favorite_bank"];
      deposits_income.value = res.data.deposit["income"];
      deposits_type.value = res.data.deposit["invest_type"];
      savings_age.value = res.data.saving["age"];
      savings_balance.value = res.data.saving["balance"];
      savings_bank.value = res.data.saving["favorite_bank"];
      savings_income.value = res.data.saving["income"];
      savings_type.value = res.data.saving["invest_type"];
    })
    .catch((err) => console.log(err));
});
</script>

<style scoped>
.container {
  width: 90%;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
}
</style>
