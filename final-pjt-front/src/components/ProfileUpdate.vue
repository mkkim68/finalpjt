<template>
  <div class="container">
    <h1>회원정보 수정</h1>
    <form id="memberForm" @submit.prevent="userUpdate">
      <div class="guide">
        <span class="important">*</span> 별표 표시는
        <span class="important">필수</span> 입력 항목입니다.
      </div>
      <table>
        <tr>
          <th>
            <span class="important">* </span>
            <label for="username">아이디</label>
          </th>
          <td>
            <input type="text" id="username" v-model.trim="username" />
          </td>
        </tr>
        <tr>
          <th>
            <span class="important">* </span>
            <label for="email">이메일</label>
          </th>
          <td><input type="email" id="email" v-model.trim="email" /><br /></td>
        </tr>
        <tr>
          <th>
            <span class="important">* </span>
            <label for="password1">비밀번호</label>
          </th>
          <td>
            <input
              type="password"
              id="password1"
              v-model.trim="password1"
            /><br />
            <span style="font-size: 0.7em"
              >※ 대문자, 숫자, "~!@#()_|. 특수기호를 포함한 3~5자</span
            >
          </td>
        </tr>
        <tr>
          <th>
            <span class="important">* </span>
            <label for="password2">비밀번호 확인</label>
          </th>
          <td>
            <input type="password" id="password2" v-model.trim="password2" />
          </td>
        </tr>
        <tr>
          <th>
            <label for="age">나이</label>
          </th>
          <td>
            <input type="number" id="age" v-model="age" />
          </td>
        </tr>
        <tr>
          <th>
            <label for="balance">잔액(만원 단위)</label>
          </th>
          <td>
            <input type="number" id="balance" v-model="balance" />
          </td>
        </tr>
        <tr>
          <th>
            <label for="income">연봉(만원 단위)</label>
          </th>
          <td>
            <input type="number" id="income" v-model="income" />
          </td>
        </tr>
        <tr>
          <th>
            <label for="favorite_bank">주거래 은행</label>
          </th>
          <td>
            <select id="favorite_bank" v-model="favorite_bank">
              <option disabled>은행을 선택해주세요</option>
              <option value="0010001">우리은행</option>
              <option value="0010927">국민은행</option>
              <option value="0011625">신한은행</option>
              <option value="0010002">한국스탠다드차타드은행</option>
              <option value="0010006">한국씨티은행</option>
              <option value="0013909">하나은행</option>
              <option value="0013175">농협</option>
              <option value="0015130">카카오뱅크</option>
              <option value="0017801">토스뱅크</option>
              <option value="0010016">대구은행</option>
              <option value="0010017">부산은행</option>
              <option value="0010019">광주은행</option>
              <option value="0010020">제주은행</option>
              <option value="0014807">수협은행</option>
            </select>
          </td>
        </tr>
        <tr>
          <th>
            <label for="invest_type">저축성향</label>
          </th>
          <td>
            <select v-model="invest_type" id="invest_type">
              <option disabled>저축성향을 입력하세요</option>
              <option value="알뜰">알뜰형</option>
              <option value="도전">도전형</option>
              <option value="성실">성실형</option>
            </select>
          </td>
        </tr>
      </table>
      <div class="buttons">
        <input type="submit" value="회원정보 수정" />
      </div>
    </form>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const route = useRoute();
const user_id = ref(route.params.user_id);
const authStore = useAuthStore();

const username = ref(null);
const email = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const age = ref(null);
const balance = ref(null);
const income = ref(null);
const favorite_bank = ref(null);
const invest_type = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: `${authStore.API_URL}/accounts/${user_id.value}/`,
    headers: {
      Authorization: `Token ${authStore.token}`,
    },
  })
    .then((res) => {
      username.value = res.data.username;
      email.value = res.data.email;
      password1.value = res.data.password1;
      password2.value = res.data.password2;
      age.value = res.data.age;
      balance.value = res.data.balance;
      income.value = res.data.income;
      favorite_bank.value = res.data.favorite_bank;
      invest_type.value = res.data.invest_type;
    })
    .catch((err) => console.log(err));
});

const userUpdate = function () {
  const payload = {
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    balance: balance.value,
    income: income.value,
    favorite_bank: favorite_bank.value,
    invest_type: invest_type.value,
    user_id: user_id.value,
  };
  authStore.userUpdate(payload);
};
</script>

<style lang="scss" scoped></style>
