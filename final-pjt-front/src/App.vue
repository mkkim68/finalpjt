<template>
  <header>
    <nav>
      <div class="menu">
        <span class="logo">
          <RouterLink to="/">
            <img class="icon logo" src="@/assets/logo.png" alt="product" />
          </RouterLink>
        </span>
        <RouterLink :to="{ name: 'DepositList' }" active-class="active">
          <img class="icon product" src="@/assets/product.png" alt="product" />
          <span class="link-text">예적금</span>
        </RouterLink>
        <RouterLink :to="{ name: 'ExchangeView' }" active-class="active">
          <img
            class="icon exchange"
            src="@/assets/exchange.png"
            alt="product"
          />
          <span class="link-text">환율</span>
        </RouterLink>
        <RouterLink :to="{ name: 'MapView' }" active-class="active">
          <img class="icon map" src="@/assets/map.png" alt="product" />
          <span class="link-text">지도</span>
        </RouterLink>
        <RouterLink :to="{ name: 'community' }" active-class="active">
          <img
            class="icon community"
            src="@/assets/community.png"
            alt="product"
          />
          <span class="link-text">게시판</span>
        </RouterLink>
        <RouterLink :to="{ name: 'ChartView' }" active-class="active">
          <img class="icon chart" src="@/assets/chart.png" alt="product" />
          <span class="link-text">차트</span>
        </RouterLink>

        <span class="user" v-if="!authStore.isLogin">
          <RouterLink :to="{ name: 'SignUpView' }">
            <span>회원가입</span>
          </RouterLink>
          <span> | </span>
          <RouterLink :to="{ name: 'LogInView' }">
            <span>로그인</span>
          </RouterLink>
        </span>
        <span class="user" v-else>
          <RouterLink
            :to="{
              name: 'ProfileView',
              params: { user_id: authStore.info?.id || 'default' },
            }"
            class="hi"
            v-if="authStore.info"
          >
            <span>{{ authStore.info.username }}님 안녕하세요</span>
          </RouterLink>

          <span> | </span>
          <a @click="authStore.logOut"><span>로그아웃</span></a>
        </span>
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
      <button @click="toggleChat">X</button>
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

onMounted(() => {
  nextTick(scrollToBottom);
});
</script>

<style scoped>
img.logo {
  width: 80px;
}

img.icon {
  width: 50px;
  margin-right: 0px;
}

img.product {
  width: 45px;
  margin-right: 3px;
}

img.map {
  margin-right: -5px;
}

div.menu {
  background-color: #e4f9e9;
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

span.logo {
  padding-left: 15px;
  margin-right: 30px;
}

span.user > a {
  text-decoration: none;
  color: black;
  font-size: medium;
}

a:link,
a:visited {
  text-decoration: none;
}

a:hover > span {
  color: #13bd7e;
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

a.hi:hover span {
  display: inline-block;
  font-weight: bolder;
  opacity: 1;
  animation: waveEffect 3s ease-in-out forwards;
  align-items: center;
}

@keyframes waveEffect {
  0% {
    opacity: 1;
    color: black;
    align-items: center;
  }
  50% {
    opacity: 1;
    color: #5d87ff;
    font-size: 1.2em;
    align-items: center;
  }
  100% {
    opacity: 1;
    color: black;
    align-items: center;
  }
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
  margin: 0px 10px;
}

/* 챗봇 */
/* styles.css */
#chatbot-icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #007bff;
  color: white;
  border-radius: 50%;
  padding: 15px;
  cursor: pointer;
  z-index: 1000;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
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
  opacity: 0.85;
}

#chatbot-header {
  background-color: #007bff;
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
}

#chatbot-input input {
  flex: 1;
  border: none;
  padding: 10px;
  outline: none;
}

#chatbot-input button {
  border: none;
  background-color: #007bff;
  color: white;
  padding: 10px;
  cursor: pointer;
}

.hidden {
  display: none !important;
}
</style>
