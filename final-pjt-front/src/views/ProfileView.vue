// ProfileView.vue

<template>
  <div v-if="info" class="container">
    <h1>{{ info.user.username }}'s Profile</h1>
    <RouterLink
      v-if="Number(authStore.info.id) === Number(user_id)"
      :to="{ name: 'ProfileUpdate' }"
      >개인정보 수정</RouterLink
    >
    <div>
      <p>email: {{ info.user.email ? info.user.email : "미기입" }}</p>
      <p>age: {{ info.user.age ? info.user.age : "미기입" }}</p>
      <p>잔고: {{ info.user.balance ? info.user.balance + "원" : "미기입" }}</p>
      <p>연봉: {{ info.user.income ? info.user.income + "원" : "미기입" }}</p>
      <p>주거래은행: {{ info.user.favorite_bank ? info.user.favorite_bank : "미기입" }}</p>
      <p>저축 유형: {{ info.user.invest_type ? info.user.invest_type + "형" : "미기입" }}</p>
    </div>
    <div>
      <h4>가입 중인 예금 상품</h4>
      <ul>
        <li v-for="deposit in deposits" :key="deposit.deposit.id">
          {{ deposit.deposit.fin_prdt_nm }}
        </li>
      </ul>
      <canvas id="depositsChart"></canvas>
    </div>
    <div>
      <h4>가입 중인 적금 상품</h4>
      <ul>
        <li v-for="saving in savings" :key="saving.saving.id">
          {{ saving.saving.fin_prdt_nm }}
        </li>
      </ul>
      <canvas id="savingsChart"></canvas>
    </div>
  </div>
  <div v-else>
    <p>로그인이 필요합니다.</p>
  </div>
  <RouterView />
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";
import { useChartStore } from "@/stores/chart";  // Chart.js 기능을 불러옵니다
import { onMounted, ref, nextTick } from "vue";  // nextTick을 불러옵니다
import { useRoute, useRouter, RouterLink, RouterView } from "vue-router";
import axios from "axios";

const authStore = useAuthStore();
const chartStore = useChartStore();  // Chart.js 기능을 사용합니다
const route = useRoute();
const router = useRouter();
const user_id = ref(route.params.user_id || authStore.info?.id);
const info = ref(null);
const deposits = ref([]);
const savings = ref([]);

onMounted(() => {
  if (user_id.value) {
    axios({
      method: "get",
      url: `${authStore.API_URL}/accounts/${user_id.value}/`,
      headers: {
        Authorization: `Bearer ${authStore.token}`
      }
    })
      .then(async (res) => {
        console.log(res.data);
        info.value = res.data;
        deposits.value = res.data.deposits;
        savings.value = res.data.savings;
        
        await nextTick();
        if (deposits.value.length > 0) {
          chartStore.drawChart('depositsChart', deposits.value, '저축 금리', '최고 우대 금리');
        }
        if (savings.value.length > 0) {
          chartStore.drawChart('savingsChart', savings.value, '저축 금리', '최고 우대 금리');
        }
      })
      .catch((err) => {
        console.log(err);
        if (err.response.status === 401) {
          router.push("/login");
        }
      });
  } else {
    console.error("Missing user_id");
    router.push("/login");
  }
});
</script>
