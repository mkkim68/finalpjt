<template>
  <div class="container">
    <h1>Home Page</h1>

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
                <img src="@/assets/map.png" alt="product1" class="product">
            </div>
            <div class="carousel-item">
              <img src="@/assets/exchange.png" alt="product2" class="product">
            </div>
            <div class="carousel-item">
              <img src="@/assets/chart.png" alt="product3" class="product">
            </div>
          </div>
      
          <!-- Left and right controls/icons -->
          <button class="carousel-control-prev" type="button" data-bs-target="#demo" data-bs-slide="prev">
            <span class="carousel-control-prev-icon"></span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#demo" data-bs-slide="next">
            <span class="carousel-control-next-icon"></span>
          </button>
      </div> <!-- end.carousel -->		

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



div.carousel {
	border : 2px solid #4caf50;
  border-radius: 10px;
  background-color: lightgray;
}
div.carousel-item > img {
  height: 90%;
}

</style>
