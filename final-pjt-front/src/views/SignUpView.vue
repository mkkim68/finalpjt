<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username: </label>
      <input type="text" id="username" v-model.trim="username" /><br />

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
      {{ favorite_bank }}
      <label for="favorite_bank">favorite bank(만 단위): </label>
      <select type="number" id="favorite_bank" v-model="favorite_bank">
        <option disabled>은행을 선택해주세요</option>
        <option value="0010001">우리은행</option>
        <option value="0010002">한국스탠다드차타드은행</option>
        <option value="0010006">한국씨티은행</option>
        <option value="hana">하나은행</option>
        <option value="nonghyup">농협</option>
        <option value="kakaobank">카카오뱅크</option></select
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
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    balance: balance.value,
    income: income.value,
  };
  store.signUp(payload);
};
</script>

<style></style>
