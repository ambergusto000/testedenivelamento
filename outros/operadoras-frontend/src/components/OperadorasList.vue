<template>
  <div class="operadoras-list">
    <div v-if="loading" class="loading">Carregando...</div>
    
    <ul v-else>
      <li v-for="op in operadoras" :key="op.id" class="operadora-item">
        <h3>{{ op.nome_fantasia }}</h3>
        <p><strong>CNPJ:</strong> {{ op.cnpj }}</p>
        <p><strong>Local:</strong> {{ op.cidade }}/{{ op.uf }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  operadoras: Array,
  loading: Boolean
});
</script>

<style scoped>
.operadora-item {
  background: #f5f5f5;
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 4px;
}
.loading {
  text-align: center;
  padding: 20px;
}
</style>