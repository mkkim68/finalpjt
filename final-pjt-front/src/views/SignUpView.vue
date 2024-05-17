<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username: </label>
      <input type="text" id="username" v-model.trim="username" /><br />

      <label for="email">email: </label>
      <input type="email" id="email" v-model.trim="email" /><br />

      <label for="password1">password: </label>
      <input type="password" id="password1" v-model.trim="password1" /><br />

      <label for="password2">password confirmation: </label>
      <input type="password" id="password2" v-model.trim="password2" />

      <p>선택 사항</p>
      <label for="age">age: </label>
      <input type="number" id="age" v-model="age" /><br />

      <label for="balance">balance(만 단위): </label>
      <input type="number" id="balance" v-model="balance" /><br />

      <label for="income">income(만 단위): </label>
      <input type="number" id="income" v-model="income" /><br />

      <label for="favorite_bank">favorite bank: </label>
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
        <option value="0014807">수협은행</option></select
      ><br />

      <label for="invest_type">저축성향: </label>
      <select v-model="invest_type" id="invest_type">
        <option disabled>저축성향을 입력하세요</option>
        <option value="알뜰">알뜰형</option>
        <option value="도전">도전형</option>
        <option value="성실">성실형</option></select
      ><br />

      <label for="income">income(만 단위): </label>
      <input type="number" id="income" v-model="income" /><br />

      <input type="submit" value="SignUp" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";

const username = ref(null);
const email = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const age = ref(null);
const balance = ref(null);
const income = ref(null);
const favorite_bank = ref(null);
const invest_type = ref(null);

const store = useAuthStore();

const signUp = function () {
  const payload = {
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    balance: balance.value,
    income: income.value,
    invest_type: invest_type.value,
  };
  store.signUp(payload);
};
</script>

<style></style>
