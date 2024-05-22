// ProfileView.vue
<template>
  <div v-if="info" class="container">
    <h1>{{ info.username }}'s Profile</h1>
    <RouterLink
      v-if="Number(authStore.info.id) === Number(user_id)"
      :to="{ name: 'ProfileUpdate' }"
      >개인정보 수정</RouterLink
    >
    <div>
      <p>email: {{ info.email ? info.email : "미기입" }}</p>
      <p>age: {{ info.age ? info.age : "미기입" }}</p>
      <p>잔고: {{ info.balance ? info.balance + "원" : "미기입" }}</p>
      <p>연봉: {{ info.income ? info.income + "원" : "미기입" }}</p>
      <p>
        주거래은행: {{ info.favorite_bank ? info.favorite_bank : "미기입" }}
      </p>
      <p>
        저축 유형: {{ info.invest_type ? info.invest_type + "형" : "미기입" }}
      </p>
    </div>
    <div>
      <h4>가입 중인 예금 상품</h4>
      <ul>
        <li v-for="deposit in deposits" :key="deposit.id">
          {{ deposit.fin_prdt_nm }}
        </li>
      </ul>
    </div>
    <div>
      <h4>가입 중인 적금 상품</h4>
      <ul>
        <li v-for="saving in savings" :key="saving.id">
          {{ saving.fin_prdt_nm }}
        </li>
      </ul>
    </div>
    <div>
      <h4>추천 예금 상품</h4>
      <canvas id="depositChart"></canvas>
    </div>
  </div>
  <div v-else>
    <p>로그인이 필요합니다.</p>
  </div>
  <RouterView />
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";
import { useProductStore } from "@/stores/product";
import { onMounted, ref } from "vue";
import { useRoute, useRouter, RouterLink, RouterView } from "vue-router";
import axios from "axios";
import { Chart } from "chart.js";

const authStore = useAuthStore();
const productStore = useProductStore();
const route = useRoute();
const router = useRouter();
const user_id = ref(route.params.user_id || authStore.info?.id);
const info = ref(null);
const deposits = ref([]);
const savings = ref([]);
const recommendations = ref([]);

const getDepositRecommendations = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/deposit_recommend/${user_id.value}/`);
    recommendations.value = response.data.age_recommendations;
    drawChart(recommendations.value);
  } catch (err) {
    console.error(err);
  }
};

const drawChart = async (recommendations) => {
  const depositNames = [];
  for (const id of recommendations) {
    const deposit = await axios.get(`${authStore.API_URL}/deposits/${id}/`);
    depositNames.push(deposit.data.fin_prdt_nm);
  }

  const ctx = document.getElementById('depositChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: depositNames,
      datasets: [{
        label: 'Top 3 Recommended Deposits',
        data: Array(recommendations.length).fill(1),  // Assuming we just want to show the top 3 without counts
        backgroundColor: ['rgba(75, 192, 192, 0.2)'],
        borderColor: ['rgba(75, 192, 192, 1)'],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            precision: 0  // Ensure the ticks are integer values
          }
        }
      }
    }
  });
};


onMounted(() => {
  if (user_id.value) {
    axios({
      method: "get",
      url: `${authStore.API_URL}/accounts/${user_id.value}/`,
    })
      .then((res) => {
        console.log(res.data);
        info.value = res.data;
        for (const item of res.data.deposit) {
          deposits.value.push(productStore.deposits.find((d) => d.id == item));
        }
        for (const item of res.data.saving) {
          savings.value.push(productStore.savings.find((s) => s.id == item));
        }
      })
      .catch((err) => console.log(err));
  } else {
    console.error("Missing user_id");
    router.push("/login"); // user_id가 없는 경우 로그인 페이지로 리다이렉트
  }
});
</script>

<style scoped></style>
