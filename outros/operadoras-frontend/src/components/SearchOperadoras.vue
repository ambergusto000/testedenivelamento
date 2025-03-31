<template>
  <div class="search-box">
    <input
      type="text"
      v-model="searchTerm"
      @input="handleInput"
      placeholder="Digite nome, CNPJ ou cidade..."
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';

const searchTerm = ref('');
const emit = defineEmits(['search']);

const handleInput = () => {
  emit('search', searchTerm.value);
};
</script>

<style scoped>
.search-box {
  margin: 20px 0;
}
input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
}
</style>