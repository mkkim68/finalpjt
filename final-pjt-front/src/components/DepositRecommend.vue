<template>
  <div class="container">
    <div class="option" v-if="favorite_bank">
      <h3>
        {{ authStore.info.username }}님의 주거래은행
        <span>{{ productStore.banks[authStore.info.favorite_bank] }}</span
        >의 상품들
      </h3>
      <p v-for="deposit in deposits_bank" :key="deposit.fin_prdt_cd">
        <RouterLink
          style="text-decoration: none"
          :to="{
            name: 'DepositDetail',
            params: { fin_prdt_cd: deposit.fin_prdt_cd },
          }"
          >{{ deposit.fin_prdt_nm }}</RouterLink
        >
      </p>
    </div>
    <div class="option" v-if="age">
      <h3>
        <span>{{ Math.floor(authStore.info.age / 10) * 10 }}대</span>는 이
        상품을 선택했어요
      </h3>
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
    <div class="option" v-if="income">
      <h3>
        {{ authStore.info.username }}님과 <span>수입</span>이 비슷한 사람들은 이
        상품을 선택했어요
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
    <div class="option" v-if="balance">
      <h3>
        {{ authStore.info.username }}님과 <span>재산</span>이 비슷한 사람들은 이
        상품을 선택했어요
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
    <div class="option" v-if="invest_type">
      <h3>
        저축 성향이 <span>{{ authStore.info.invest_type }}형</span>인 사람들은
        이 상품을 선택했어요
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
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useChartStore } from "@/stores/chart";
import { useAuthStore } from "@/stores/auth";
import { useProductStore } from "@/stores/product";
import { RouterLink } from "vue-router";
import axios from "axios";

const chartStore = useChartStore();
const authStore = useAuthStore();
const productStore = useProductStore();
const API_URL = "http://127.0.0.1:8000";

const props = defineProps({
  age: Boolean,
  income: Boolean,
  balance: Boolean,
  invest_type: Boolean,
  favorite_bank: Boolean,
});

const deposits_age = ref(null);
const deposits_balance = ref(null);
const deposits_bank = ref(null);
const deposits_income = ref(null);
const deposits_type = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: `${API_URL}/api/banks/recommend/${authStore.info.id}/`,
    headers: {
      Authorization: `Token ${authStore.token}`,
    },
  })
    .then((res) => {
      deposits_age.value = res.data.deposit["age"];
      deposits_balance.value = res.data.deposit["balance"];
      deposits_bank.value = res.data.deposit["favorite_bank"];
      deposits_income.value = res.data.deposit["income"];
      deposits_type.value = res.data.deposit["invest_type"];
    })
    .catch((err) => console.log(err));
});
</script>

<style scoped>
span {
  color: #4696ff;
}
.option {
  margin-bottom: 20px;
}
h3 {
  margin: 5px;
}
p {
  background-color: aliceblue;
  margin: 0;
  padding: 10px;
  border-bottom: 1px solid #4696ff;
}
p > a {
  text-decoration: none;
}
</style>
