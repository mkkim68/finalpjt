<template>
  <div class="container">
    <h1>로그인</h1>
    <form id="memberForm" @submit.prevent="logIn">
      <div class="loginForm">
        <table>
          <tr>
            <th>
              <label for="username">아이디: </label>
            </th>
            <td>
              <input type="text" id="username" v-model.trim="username" />
            </td>
          </tr>
          <tr>
            <th>
              <label for="password">비밀번호: </label>
            </th>
            <td>
              <input type="password" id="password" v-model.trim="password" />
            </td>
          </tr>
        </table>
        <div class="buttons">
          <input type="submit" value="로그인" />
        </div>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";

const username = ref(null);
const password = ref(null);

const store = useAuthStore();

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style scoped>
.container {
  width: 90%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin: 20px auto;
}

#memberForm {
	background-color: #f2f2f2;
	border-radius: 10px;
	margin-bottom: 50px;
	padding:15px 60px;
	width: 955px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

table {
	margin-top: 20px;
	background-color:rgb(210, 210, 210);
	margin : 60px 10px 10px 0;
	border-radius: 10px;
}
th {
	padding : 50px 0 60px 50px;
}
td {
	width : 400px;
	padding : 10px 70px 10px 60px;
}
td > input {
	height : 50px;
	width : 300px;
}

div.buttons {
	display: flex;
  flex-direction: column;
	align-items: center;
}

div.buttons > input {
  padding: 10px 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 80px;
  margin-top: 20px;
}

</style>
