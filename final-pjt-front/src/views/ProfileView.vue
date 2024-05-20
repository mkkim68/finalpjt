<template>
  <div v-if="info">
    <h1>{{ info.username }}'s Profile</h1>
    <div>
      <p>email: {{ info.email ? info.email : "미기입" }}</p>
      <p>age: {{ info.age ? info.age : "미기입" }}</p>
      <p>잔고: {{ info.balance ? info.balance + "만원" : "미기입" }}</p>
      <p>연봉: {{ info.income ? info.income + "만원" : "미기입" }}</p>
      <p>
        주거래은행: {{ info.favorite_bank ? info.favorite_bank : "미기입" }}
      </p>
      <p>
        저축 유형: {{ info.invest_type ? info.invest_type + "형" : "미기입" }}
      </p>
    </div>
    <div>
      <h4>가입 중인 예금</h4>
      <ul>
        <li v-for="deposit in info.deposit" :key="deposit.fin_prdt_cd">
          {{ deposit.fin_prdt_nm }}
        </li>
      </ul>
    </div>
    <div>
      <h4>가입 중인 적금</h4>
      <ul>
        <li v-for="saving in info.saving" :key="saving.fin_prdt_cd">
          {{ saving.fin_prdt_nm }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
const authStore = useAuthStore();
const route = useRoute();
const user_id = ref(route.params.user_id);
const info = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: `${authStore.API_URL}/accounts/${user_id.value}/`,
  })
    .then((res) => {
      info.value = res.data;
    })
    .catch((err) => console.log(err));
});
</script>

<style lang="scss" scoped></style>
