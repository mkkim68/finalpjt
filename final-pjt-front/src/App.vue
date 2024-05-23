<template>
  <header>
    <nav class="navbar navbar-expand-lg" style="padding: 0">
      <div
        class="container-fluid"
        style="padding: 10px 10px; background-color: rgb(255, 255, 255)"
      >
        <RouterLink to="/" class="navbar-brand">
          <img class="icon" src="@/assets/coin_forest_icon.png" alt="product" />
          <img class="logo" src="@/assets/coin_forest_logo.png" alt="product" />
          
        </RouterLink>
        <button
          id="toggler"
          class="navbar-toggler toggler"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item choice">
              <RouterLink
                class="nav-link"
                :to="{ name: 'DepositList' }"
                active-class="active"
              >
                <!-- <img
                  class="icon leaf"
                  src="@/assets/leaf.png"
                  alt="leaf"
                  style="width: 50px"
                  active-class="active"
                /> -->
                <span class="link-text">예적금</span>
              </RouterLink>
            </li>
            <li class="nav-item choice">
              <RouterLink
                class="nav-link"
                :to="{ name: 'ExchangeView' }"
                active-class="active"
              >
                <!-- <img
                  class="icon leaf"
                  src="@/assets/leaf.png"
                  alt="leaf"
                  style="width: 50px"
                  active-class="active"
                /> -->
                <span class="link-text">환율</span>
              </RouterLink>
            </li>
            <li class="nav-item choice">
              <RouterLink
                class="nav-link"
                :to="{ name: 'MapView' }"
                active-class="active"
              >
                <!-- <img class="icon map" src="@/assets/map.png" alt="product" /> -->
                <span class="link-text">지도</span>
              </RouterLink>
            </li>
            <li class="nav-item choice">
              <RouterLink
                class="nav-link"
                :to="{ name: 'community' }"
                active-class="active"
              >
                <!-- <img
                  class="icon community"
                  src="@/assets/community.png"
                  alt="product"
                /> -->
                <span class="link-text">게시판</span>
              </RouterLink>
            </li>
            <li class="nav-item choice">
              <RouterLink
                class="nav-link"
                :to="{ name: 'ChartView' }"
                active-class="active"
              >
                <!-- <img
                  class="icon chart"
                  src="@/assets/chart.png"
                  alt="product"
                /> -->
                <span class="link-text">상품 추천</span>
              </RouterLink>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
                >{{
                  authStore.isLogin
                    ? `${authStore.info.username}님 안녕하세요`
                    : "로그인 해주세요"
                }}</a
              >
              <ul class="user dropdown-menu">
                <li v-if="!authStore.isLogin">
                  <RouterLink
                    :to="{ name: 'SignUpView' }"
                    class="dropdown-item"
                    v-if="!authStore.isLogin"
                  >
                    <span>회원가입</span>
                  </RouterLink>
                </li>
                <li v-if="!authStore.isLogin">
                  <RouterLink :to="{ name: 'LogInView' }" class="dropdown-item">
                    <span>로그인</span>
                  </RouterLink>
                </li>
                <li v-if="authStore.isLogin">
                  <RouterLink
                    :to="{
                      name: 'ProfileView',
                      params: { user_id: authStore.info?.id || 'default' },
                    }"
                    class="hi dropdown-item"
                    v-if="authStore.info"
                  >
                    <span class="wavy"
                      >{{ authStore.info.username }}의 프로필</span
                    >
                  </RouterLink>
                </li>
                <li v-if="authStore.isLogin">
                  <a class="dropdown-item" @click="authStore.logOut"
                    ><span>로그아웃</span></a
                  >
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <RouterView />

  <!-- Chatbot icon -->
  <div id="chatbot-icon" @click="toggleChat">💬</div>

  <!-- Chatbot window -->
  <div id="chatbot-window" :class="{ hidden: !chatVisible }">
    <div id="chatbot-header">
      <span>Hi Chatbot</span>
      <button @click="toggleChat" class="chat-x">X</button>
    </div>
    <div id="chatbot-messages">
      <div v-for="message in messages" :key="message.id" :class="message.type">
        {{ message.text }}
      </div>
    </div>
    <div id="chatbot-input">
      <input
        id="chat-input"
        type="text"
        v-model="userInput"
        placeholder="메시지를 입력하세요..."
        @keyup.enter="sendMessageWithRateLimit"
      />
      <button @click="sendMessageWithRateLimit">전송</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from "vue";
import { useAuthStore } from "@/stores/auth";
import axios from "axios";

const authStore = useAuthStore();

const chatVisible = ref(false);
const messages = ref([]);
const userInput = ref("");
const isSendingMessage = ref(false);
let lastRequestTime = 0;

const toggleChat = () => {
  chatVisible.value = !chatVisible.value;
};

const scrollToBottom = () => {
  const messagesContainer = document.getElementById("chatbot-messages");
  if (messagesContainer) {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
};

const sendMessage = async () => {
  if (userInput.value.trim() === "") return;
  if (isSendingMessage.value) {
    console.log("A message is already being sent, please wait.");
    return;
  }

  isSendingMessage.value = true;

  const userMessage = {
    id: Date.now(),
    text: userInput.value,
    type: "input",
  };
  messages.value.push(userMessage);

  nextTick(scrollToBottom);

  try {
    const response = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      {
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: userInput.value }],
        max_tokens: 150,
      },
      {
        headers: {
          Authorization: `Bearer ${import.meta.env.VITE_OPENAI_API_KEY}`,
          "Content-Type": "application/json",
        },
      }
    );

    const botMessage = {
      id: Date.now() + 1,
      text: response.data.choices[0].message.content.trim(),
      type: "bot",
    };
    messages.value.push(botMessage);
    nextTick(scrollToBottom);
  } catch (error) {
    const errorMessage = {
      id: Date.now() + 2,
      text:
        error.response?.status === 429
          ? "Error: Too many requests. Please wait a few seconds before trying again."
          : "Error: Could not get response from the chatbot.",
      type: "error",
    };
    messages.value.push(errorMessage);
    nextTick(scrollToBottom);

    if (error.response?.status === 429) {
      lastRequestTime = Date.now();
    }
  }

  userInput.value = "";
  isSendingMessage.value = false;
};

const REQUEST_INTERVAL = 5000; // 5초 간격

const sendMessageWithRateLimit = () => {
  const now = Date.now();
  if (now - lastRequestTime > REQUEST_INTERVAL) {
    lastRequestTime = now;
    sendMessage();
  } else {
    const errorMessage = {
      id: Date.now(),
      text: `Too many requests. Please wait ${Math.ceil(
        (REQUEST_INTERVAL - (now - lastRequestTime)) / 1000
      )} seconds before trying again.`,
      type: "error",
    };
    messages.value.push(errorMessage);
    nextTick(scrollToBottom);
  }
};

import { useProductStore } from "./stores/product";
const productStore = useProductStore();
onMounted(() => {
  nextTick(scrollToBottom);
  productStore.getDeposits();
  productStore.getSavings();
});
</script>

<style scoped>
.toggler:focus {
  outline: none !important;
}
img.icon {
  width: 80px;
}
@keyframes coinEffect {
  0% {
    transform: rotateY(200deg);
  }
  15% {
    transform: rotateY(300deg);
  }
  30% {
    transform: rotateY(520deg);
  }
  50% {
    transform: rotateY(1000deg);
  }
  70% {
    transform: rotateY(520deg);
  }
  85% {
    transform: rotateY(200deg);
  }
  100% {
    transform: rotateY(100deg);
  }
}
img.icon:hover {
  animation: coinEffect 1.5s ease-in-out infinite forwards;
}

img.icon {
  width: 80px;
  margin-right: 0px;
}

img.logo {
  width: 120px;
}

img.product {
  width: 45px;
  margin-right: 3px;
}

img.map {
  margin-right: -5px;
}

div.menu {
  background-color: #eef5ff;
  display: flex;
  align-items: center;
  border-radius: 0 0 10px 10px;
  font-family: "Jua", sans-serif;
  font-weight: 400;
  font-size: 24px;
  font-style: normal;
}

div.menu > a {
  display: flex;
  flex-direction: row;
  align-items: center;
  text-decoration: none;
  color: grey;
  font-size: larger;
  font-weight: 530;
  margin: 20px 0px;
  padding: 5px;
  width: 200px;
}

div.menu > a > span {
  width: 80px;
}

div.menu > a > img {
  padding: 0 5px;
}
span {
  text-align: center;
  padding: 0;
  margin: 0;
}
span.logo {
  padding-left: 15px;
  margin-right: 30px;
}

span.user > a {
  text-decoration: none;
  color: black;
  font-size: medium;
}
a {
  text-align: start;
}
a:link,
a:visited {
  text-decoration: none;
}

a:hover > span {
  color: #7bbd8a;
  cursor: pointer;
}

a:active > span {
  font-weight: 2em;
}

a.hi {
  overflow: hidden;
  white-space: nowrap;
  display: inline-block;
}

/* a.hi:hover span {
  display: inline-block;
  font-weight: bolder;
  opacity: 1;
  animation: waveEffect 3s ease-in-out forwards;
  align-items: center;
  z-index: 99;
} */

@keyframes waveEffect {
  0% {
    top: 0px;
  }
  50% {
    top: -15px;
  }
  100% {
    top: 0px;
  }
}

.wavy:hover {
  animation-name: waveEffect;
  animation-duration: 1.3s;
  animation-timing-function: ease;
  animation-iteration-count: infinite;
  position: relative;
  top: 0;
  left: 0;
}

.active {
  font-weight: bold;
  color: #4caf50;
}

.link-text {
  color: grey;
}

.active .link-text {
  color: #4caf50;
}

span.user {
  margin: 0px 100px 0px auto;
  min-width: 200px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

span > span {
  margin: 0px 20px;
}


span.link-text {
  font-size: larger;
  padding: 20px;
  font-weight: bold;
}

.navbar-nav {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

/* 메뉴 */
li.choice {
  /* font-family: "Nanum Gothic", sans-serif; */
  font-size: 1.1em;
  font-style: normal;
}

li.dropdown {
  margin-left: auto;
  margin-right: 50px;
}


/* 챗봇 */
/* styles.css */
#chatbot-icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #9acbff;
  color: white;
  border-radius: 50%;
  padding: 15px;
  cursor: pointer;
  z-index: 1000;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
#chatbot-icon:hover {
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.35);
}

#chatbot-window {
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 300px;
  height: 55%;
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  z-index: 1000;
  opacity: 0.95;
}

#chatbot-header {
  background-color: #77b9ff;
  color: white;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

#chatbot-messages {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.input {
  background-color: #e1ffc7;
  align-self: flex-end;
  text-align: right;
  border-radius: 10px;
  padding: 10px;
  margin: 5px;
  max-width: 80%;
}

.bot {
  background-color: #f1f1f1;
  align-self: flex-start;
  text-align: left;
  border-radius: 10px;
  padding: 10px;
  margin: 5px;
  max-width: 80%;
}

#chatbot-input {
  display: flex;
  border-top: 1px solid #ccc;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 0 0 10px 10px;
}

#chatbot-input input {
  flex: 1;
  border: none;
  padding: 10px;
  outline: none;
  border-radius: 10px 0 0 10px;
}
#chatbot-input input:focus {
  border: 1px solid #82beff;
  border-right: none;
}

#chatbot-input button {
  border: 1px solid #82beff;
  background-color: #82beff;
  color: white;
  padding: 10px;
  cursor: pointer;
  border-radius: 0 10px 10px 0;
}
#chatbot-input button:hover {
  background-color: #64afff;
}
.chat-x {
  outline: none;
  border: none;
  border-radius: 5px;
}
.chat-x:hover {
  color: #55a7ff;
}

.hidden {
  display: none !important;
}
menu {
  position: relative;
  width: 100%;
  background-color: #87ceeb; /* 하늘색 배경 */
}
.toggler {
  background-color: rgba(0, 0, 0, 0);
  border: none;
  outline: none;
  border-radius: 20px;
  position: relative;
  top: 0px;
}
.toggler:hover {
  border: 1px solid #4caf50;
}
</style>
