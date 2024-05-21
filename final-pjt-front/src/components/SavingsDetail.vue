<template>
  <div class="container">
    <h1>{{ saving.fin_prdt_nm }}</h1>
    <h5>{{ saving.kor_co_nm }}</h5>
    <div>
      <p>가입 대상: {{ saving.join_member }}</p>
      <p>가입 방법: {{ saving.join_way }}</p>
      <p>가입 제한: {{ join_deny }}</p>
      <p>만기 후 이자율: {{ saving.mtrt_int }}</p>
      <p>기타 유의사항: {{ saving.etc_note }}</p>
    </div>
    <div>
      <table>
        <thead style="text-align: center">
          <tr>
            <th
              class="third"
              :colspan="options.length + 1"
              style="background-color: rgb(233, 233, 233)"
            >
              금리
            </th>
          </tr>
          <tr>
            <th>금리 유형</th>
            <th v-for="option in options" :key="option.id">
              {{ option.save_trm }}개월
            </th>
          </tr>
        </thead>
        <tbody style="text-align: center">
          <tr>
            <td style="color: rgb(0, 174, 255)">저축 금리</td>
            <td v-for="option in options" :key="option.id">
              {{ option.intr_rate }}%
            </td>
          </tr>
          <tr>
            <td style="color: rgb(0, 174, 255)">최고 우대 금리</td>
            <td v-for="option in options" :key="option.id">
              {{ option.intr_rate2 }}%
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- 뒤로가기 -->
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import axios from "axios";

const route = useRoute();
const authStore = useAuthStore();

const fin_prdt_cd = ref(route.params.fin_prdt_cd);
const API_URL = "http://127.0.0.1:8000";

const saving = ref([]);
const join_deny = ref(null);
const options = ref([]);

onMounted(() => {
  axios({
    method: "get",
    url: `${API_URL}/api/banks/savings/${fin_prdt_cd.value}/`,
    headers: {
      Authorization: `Token ${authStore.token}`,
    },
  })
    .then((res) => {
      saving.value = res.data;
      if (res.data.join_deny === 1) {
        join_deny.value = "없음";
      } else if (res.data.join_deny === 2) {
        join_deny.value = "서민전용";
      } else if (res.data.join_deny === 3) {
        join_deny.value = "일부제한";
      }
      axios({
        method: "get",
        url: `${API_URL}/api/banks/savings/${fin_prdt_cd.value}/option/`,
        headers: {
          Authorization: `Token ${authStore.token}`,
        },
      })
        .then((res) => {
          console.log(res.data);
          options.value = res.data;
        })
        .catch((err) => console.log(err));
    })
    .catch((err) => console.log(err));
});
</script>

<style scoped>
.table-section {
  margin-top: 2px;
  padding: 20px;
  background-color: #f4f4f4;
  border: 1px solid #ddd;
}

.filter-section {
  flex: 1;
  max-width: 250px;
}

div.condition {
  margin: 20px 10px;
}

form > div > select {
  width: 100%;
  height: 30px;
  padding: 1px 0px;
  cursor: pointer;
}

.table-section {
  flex: 2;
  width: 100%;
}

table {
  width: 100%;
  border: 1px solid black;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ccc;
  padding: 10px;
  font-size: 0.8em;
}
th.plus {
  width: 14%;
}

th.first {
  width: 16%;
}

th.second {
  width: 25%;
}

th.third {
  width: 22%;
}
</style>
