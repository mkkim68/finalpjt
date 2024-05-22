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
      <h4>가입한 상품 금리</h4>
      <canvas id="interestChart"></canvas>
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
import {
  Chart,
  BarController,
  BarElement,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

Chart.register(
  BarController,
  BarElement,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend
);

const authStore = useAuthStore();
const productStore = useProductStore();
const route = useRoute();
const router = useRouter();
const user_id = ref(route.params.user_id || authStore.info?.id);
const info = ref(null);
const deposits = ref([]);
const savings = ref([]);

let myChart = null;

const drawChart = (labels, data1, data2) => {
  const ctx = document.getElementById('interestChart').getContext('2d');
  
  if (myChart) {
    myChart.destroy();
  }

  myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: '저축 금리',
          data: data1,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        },
        {
          label: '최고 우대금리 금리',
          data: data2,
          backgroundColor: 'rgba(153, 102, 255, 0.2)',
          borderColor: 'rgba(153, 102, 255, 1)',
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
};

const getProductData = async () => {
  const depositData = await Promise.all(deposits.value.map(async (deposit) => {
    try {
      const response = await axios.get(`${authStore.API_URL}/api/banks/deposit-options/${deposit.fin_prdt_cd}/`);
      console.log(`Deposit options for ${deposit.fin_prdt_cd}:`, response.data);
      return response.data.map(option => ({ ...option, fin_prdt_nm: deposit.fin_prdt_nm }));
    } catch (error) {
      console.error(`Error fetching deposit options for ${deposit.fin_prdt_cd}`, error);
      return null;
    }
  }));

  const savingData = await Promise.all(savings.value.map(async (saving) => {
    try {
      const response = await axios.get(`${authStore.API_URL}/api/banks/saving-options/${saving.fin_prdt_cd}/`);
      console.log(`Saving options for ${saving.fin_prdt_cd}:`, response.data);
      return response.data.map(option => ({ ...option, fin_prdt_nm: saving.fin_prdt_nm }));
    } catch (error) {
      console.error(`Error fetching saving options for ${saving.fin_prdt_cd}`, error);
      return null;
    }
  }));

  const allData = [...depositData, ...savingData].filter(data => data !== null);

  console.log("Deposit Data:", depositData);
  console.log("Saving Data:", savingData);
  console.log("All Data:", allData);

  return allData;
};

const processData = (productData) => {
  console.log("Product Data:", productData);

  const labels = [];
  const data1 = [];
  const data2 = [];

  const productMap = new Map();

  productData.forEach(productArray => {
    if (Array.isArray(productArray)) {
      productArray.forEach(product => {
        let name = "Unknown Product";

        if (product.fin_prdt_nm) {
          name = product.fin_prdt_nm;
        }

        const rate1 = product.intr_rate !== undefined ? product.intr_rate : 0;
        const rate2 = product.intr_rate2 !== undefined ? product.intr_rate2 : 0;

        if (!productMap.has(name)) {
          productMap.set(name, { rate1, rate2 });
        }
      });
    } else {
      console.warn("Expected an array but got:", productArray);
    }
  });

  productMap.forEach((value, key) => {
    labels.push(key);
    data1.push(value.rate1);
    data2.push(value.rate2);
  });

  console.log("Labels:", labels);
  console.log("Data1 (저축 금리):", data1);
  console.log("Data2 (최고 우대금리 금리):", data2);

  drawChart(labels, data1, data2);
};

onMounted(async () => {
  if (user_id.value) {
    try {
      const res = await axios.get(`${authStore.API_URL}/accounts/${user_id.value}/`);
      info.value = res.data;
      deposits.value = res.data.deposit.map(depositId => {
        return productStore.deposits.find((d) => d.id === depositId) || {};
      }).filter(deposit => deposit.id);
      savings.value = res.data.saving.map(savingId => {
        return productStore.savings.find((s) => s.id === savingId) || {};
      }).filter(saving => saving.id);

      const productData = await getProductData();
      processData(productData);
    } catch (err) {
      console.log(err);
    }
  } else {
    console.error("Missing user_id");
    router.push("/login");
  }
});
</script>

<style scoped></style>
