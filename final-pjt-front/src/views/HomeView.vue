<template>
  <div class="container">

    <div class="contents">
      <!-- Carousel -->
      <div id="demo" class="carousel slide" data-bs-ride="carousel">
        <!-- Indicators/dots -->
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#demo" data-bs-slide-to="0" class="active"></button>
          <button type="button" data-bs-target="#demo" data-bs-slide-to="1"></button>
          <button type="button" data-bs-target="#demo" data-bs-slide-to="2"></button>
        </div>
  
        <!-- The slideshow/carousel -->
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="d-flex">
              <div class="card">
                <img src="@/assets/bank/KAKAO_Profile.png" alt="카카오뱅크" class="product">
                <div class="card-body">
                  <p class="card-text">카카오</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/TOSS_Profile.png" alt="토스뱅크" class="product">
                <div class="card-body">
                  <p class="card-text">토스</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/KB_Profile.png" alt="국민은행" class="product">
                <div class="card-body">
                  <p class="card-text">국민</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/HANA_Profile.png" alt="하나은행" class="product">
                <div class="card-body">
                  <p class="card-text">하나</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/WOORI_Profile.png" alt="우리은행" class="product">
                <div class="card-body">
                  <p class="card-text">우리</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/SHINHAN_Profile.png" alt="신한은행" class="product">
                <div class="card-body">
                  <p class="card-text">신한</p>
                </div>
              </div>
            </div>
          </div>
  
          <div class="carousel-item">
            <div class="d-flex">
              <div class="card">
                <img src="@/assets/bank/IBK_Profile.png" alt="IBK 기업은행" class="product">
                <div class="card-body">
                  <p class="card-text">IBK기업</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/KDB_Profile.png" alt="KDB 산업은행" class="product">
                <div class="card-body">
                  <p class="card-text">KDB산업</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/NH_Profile.png" alt="농협은행" class="product">
                <div class="card-body">
                  <p class="card-text">농협</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/SH_Profile.png" alt="SH수협은행" class="product">
                <div class="card-body">
                  <p class="card-text">SH수협</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/CU_Profile.png" alt="CU" class="product">
                <div class="card-body">
                  <p class="card-text">신협</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/SC_Profile.png" alt="SC제일은행" class="product">
                <div class="card-body">
                  <p class="card-text">SC제일</p>
                </div>
              </div>
            </div>
          </div>
  
          <div class="carousel-item">
            <div class="d-flex">
              <div class="card">
                <img src="@/assets/bank/EPOST_Profile.png" alt="우정사업본부" class="product">
                <div class="card-body">
                  <p class="card-text">우정</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/BUSAN_Profile.png" alt="부산은행" class="product">
                <div class="card-body">
                  <p class="card-text">부산</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/DGB_Profile.png" alt="DGB대구은행" class="product">
                <div class="card-body">
                  <p class="card-text">DGB대구</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/KWANGJU_Profile.png" alt="광주은행" class="product">
                <div class="card-body">
                  <p class="card-text">광주</p>
                </div>
              </div>
              <div class="card">
                <img src="@/assets/bank/K_Profile.png" alt="K뱅크" class="product">
                <div class="card-body">
                  <p class="card-text">K뱅크</p>
                </div>
              </div>
            </div>
          </div>
        </div>
  
        <!-- Left and right controls/icons -->
        <div class="move">
          <button class="carousel-control-prev" type="button" data-bs-target="#demo" data-bs-slide="prev">
            <span class="carousel-control-prev-icon"></span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#demo" data-bs-slide="next">
            <span class="carousel-control-next-icon"></span>
          </button>
        </div>
      </div> <!-- end.carousel -->


      <div class="info-section">
        <h3>내게 맞는 금융상품, 비교하기 힘드시죠?</h3>
        <h2 style="font-weight: bold;">코인 포레스트는 "쉽고 정확하게" 비교합니다.</h2>
        <div class="info-cards">
          <div class="info-card">
            <p style="font-weight: bold;">국내 최대 금융상품 데이터</p>
            <img class="advantage ai" src="@/assets/ai.png" alt="ai">
            <br><p>다양한 조건 필터링으로 <br>예적금 상품 조회 및 가입을 도와드립니다.</p>
          </div>
          <div class="info-card">
            <p style="font-weight: bold;">나만을 위한 금융매칭</p>
            <img class="advantage bank" src="@/assets/bank.png" alt="bank">
            <br><p>수백만가지 경우의 수를 계산하는 <strong>추천 알고리즘</strong>이<br>나를 위한 맞춤 상품을 찾아드립니다.</p>
          </div>
          <div class="info-card">
            <p style="font-weight: bold;">광고X 홍보X</p>
            <img class="advantage no_ad" src="@/assets/no_ad.png" alt="no_ad">
            <br><p>코인 포레스트의 추천에는 광고도, 홍보도 없습니다.<br>오직 객관적인 데이터만을 활용합니다.</p>
          </div>
        </div>
      </div>

    </div><!-- end.contents -->
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { RouterLink } from "vue-router";

onMounted(() => {});

</script>

<style scoped>
.container {
  width: 90%;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
}

.info-section {
  text-align: center;
  margin-bottom: 40px;
}

.info-section h3 {
  font-size: 1.2em;
  color: #666;
}

.info-section h2 {
  font-size: 1.8em;
  margin-bottom: 20px;
}

.info-cards {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-top: 50px;
}

.info-card {
  width: 30%;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
}

.info-card img {
  width: 50px;
  height: 50px;
  margin-bottom: 10px;
}

.info-card p {
  font-size: 0.9em;
  color: #333;
  line-height: 1.5em;
}

img.advantage {
  width: 30%;
  height: 30%;
}





/* carousel */
.carousel {
  margin: 20px auto;
  margin-bottom: 100px;
  /* border: 2px solid black; */
  border-radius: 10px;
  /* background-color: lightgray; */
  max-width: 700px;
  height: 200px;
  padding: 3px 20px; /* 버튼과 carousel-inner 사이의 간격 추가 */
  font-family: sans-serif;
  font-weight: 500;
}

.carousel-item {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-top: 5px;
  transition: transform 0.6s ease-in-out; /* 스무스하게 이동하는 애니메이션 추가 */
}

.carousel-item {
  visibility: hidden;
}

.carousel-item.active {
  visibility: visible;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel-item-next,
.carousel-item-prev {
  transform: translateX(100%); /* 다음 아이템은 오른쪽에서 나타남 */
}

.carousel-item-prev {
  transform: translateX(-100%); /* 이전 아이템은 왼쪽에서 나타남 */
}

.card {
  width: 100px;
  height: 120px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: white;
  margin: 5px;
  padding: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.card img {
  width: 50px;
  height: 50px;
}

.card-body {
  padding: 5px;
}

.card-text {
  font-size: 0.8em;
  margin-top: 5px;
}

.carousel-control-prev,
.carousel-control-next {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: white;
  border: 1px solid #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
  top: 80%; /* 버튼을 중간으로 내림 */
  transform: translateY(-50%); /* 정확히 가운데 정렬 */
  position: absolute;
}

.carousel-control-prev {
  left: 70px; /* 왼쪽 버튼을 Carousel 요소 쪽으로 붙임 */
}

.carousel-control-next {
  right: 70px; /* 오른쪽 버튼을 Carousel 요소 쪽으로 붙임 */
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-color: grey;
  border-radius: 50%;
  width: 20px;
  height: 20px;
}
</style>
