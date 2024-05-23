<template>
  <div class="container">
    <div class="btnGroup">
      <ul class="menu_wrap" role="tablist">
        <li class="menu_item" role="presentation">
          <RouterLink
            to="/product/deposit"
            active-class="on"
            id="dashboard"
            class="menu_id"
            role="tab"
            aria-selected="true"
          >
            <span class="text">예금</span></RouterLink
          >
        </li>
        <li class="menu_item" role="presentation">
          <RouterLink
            to="/product/savings"
            active-class="on"
            id="shop"
            class="menu_id"
            role="tab"
            aria-selected="false"
          >
            <span class="text">적금</span></RouterLink
          >
        </li>
      </ul>
    </div>
    <!-- end.btnGroup -->

    <router-view></router-view>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useProductStore } from "@/stores/product";
import { RouterLink } from "vue-router";

const store = useProductStore();

onMounted(() => {});
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  width: 90%;
  margin: 20px auto;
}

.btnGroup {
  display: flex;
  justify-content: flex-end;
  width: 100%;
  margin-top: 20px;
  padding: 0 20px;
}

a {
  color: grey;
  font-weight: normal;
  text-decoration: none;
}

.active {
  font-weight: bold;
  color: #4caf50;
}

/* 버튼 */
div.btnGroup {
  display: flex;
  width: 100%;
  height: 65px;
  border-radius: 30px 30px 0 0;
  padding: 0px;
}

ul.menu_wrap {
  box-sizing: border-box;
  display: table;
  table-layout: fixed;
  width: auto;
  height: 100%;
  border-collapse: collapse;
  list-style: none;
}

li.menu_item {
  display: table-cell;
  vertical-align: middle;
}

a.menu_id {
  display: block;
  padding: 20px 60px;
  border: 1px solid #e3e3e3;
  border-bottom: none;
  border-radius: 30px 30px 0 0;
  background-color: #ecf2ff;
  text-align: center;
  z-index: 5;
}

div.btnGroup > ul > li > a {
  text-decoration: none;
  color: black;
  background-color: white;
}

div.btnGroup > ul > li > a:hover {
  text-decoration: none;
  color: #4caf50;
}

div.btnGroup > ul > li > a.on {
  color: #4caf50;
  background-color: #f2f2f2;
  font-weight: bolder;
  text-decoration: none;
  font-size: 1.2em;
}

div.btnGroup > ul > li > a:hover > span,
div.btnGroup > ul > li > a:focus > span {
  display: inline-block;
  text-align: center;
  font-weight: bolder;
  font-size: 1.2em;
}
</style>
