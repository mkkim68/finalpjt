<template>
  <div class="container">
    <h1 style="display: flex; align-items: center">
      {{ deposit.fin_prdt_nm }}
      <button class="btn btn-primary" @click="join" v-if="!isJoined">
        가입하기
      </button>
      <button disabled class="btn btn-secondary" @click="join" v-else>
        가입 완료
      </button>
    </h1>
    <div id="product-info">
      <p>
        <span style="font-weight: 600">가입 은행 |</span>
        {{ deposit.kor_co_nm }}</p>
      <p>
        <span style="font-weight: 600">가입 대상 |</span>
        {{ deposit.join_member }}
      </p>
      <p>
        <span style="font-weight: 600">가입 방법 |</span>
        {{ deposit.join_way }}
      </p>
      <p>
        <span style="font-weight: 600">가입 제한 |</span>
        {{ join_deny }}
      </p>
      <p>
        <span style="font-weight: 600">만기 후 이자율 |</span>
        {{ deposit.mtrt_int }}
      </p>
      <p>
        <span style="font-weight: 600">기타 유의사항 |</span>
        {{ deposit.etc_note }}
      </p>
    </div>
    <div class="table">
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
import { useRoute, useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useProductStore } from "@/stores/product";
import axios from "axios";

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();
const productStore = useProductStore();

const fin_prdt_cd = ref(route.params.fin_prdt_cd);
const API_URL = "http://127.0.0.1:8000";

const deposit = ref([]);
const join_deny = ref(null);
const options = ref([]);
const isJoined = ref(false);

onMounted(() => {
  axios({
    method: "get",
    url: `${API_URL}/api/banks/deposits/${fin_prdt_cd.value}/`,
    headers: {
      Authorization: `Token ${authStore.token}`,
    },
  })
    .then((res) => {
      deposit.value = res.data;
      if (res.data.join_deny === 1) {
        join_deny.value = "없음";
      } else if (res.data.join_deny === 2) {
        join_deny.value = "서민전용";
      } else if (res.data.join_deny === 3) {
        join_deny.value = "일부제한";
      }
      authStore.getUserInfo(authStore.info.id);
      axios({
        method: "get",
        url: `${API_URL}/api/banks/deposits/${fin_prdt_cd.value}/option/`,
        headers: {
          Authorization: `Token ${authStore.token}`,
        },
      })
        .then((res) => {
          options.value = res.data;
        })
        .then(() => {
          if (authStore.info.deposit.find((item) => item == res.data.id)) {
            isJoined.value = true;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    })
    .catch((err) => {
      console.log(err);
      alert("로그인 해주세요.");
      router.replace({ name: "LogInView" });
    });
});

const join = function () {
  const payload = {
    fin_prdt_cd: deposit.value.fin_prdt_cd,
    token: authStore.token,
  };
  productStore.joinDeposit(payload);
  isJoined.value = true;
};
</script>

<style scoped>
.container {
  width: 90%;
  margin: 80px auto;
  display: flex;
  flex-direction: column;
}

#product-info {
  margin-top: 50px;
}

div.table {
  margin-top: 30px;
}

button {
  margin-left: 10px;
}
.btn-primary {
  background-color: rgb(134, 186, 255);
  border: none;
}
.btn-primary:hover {
  background-color: rgb(83, 157, 255);
}
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
