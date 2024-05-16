<template>
  <div>
    <h1>Exchange Page</h1>
    
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'


const store = useCounterStore()

onMounted(() => {
  
})

</script>

<style>

</style>
