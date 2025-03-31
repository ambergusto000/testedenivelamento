<template>
  <div class="app">
    <h1>Busca de Operadoras</h1>
    
    <div class="search-box">
      <input
        type="text"
        v-model="searchTerm"
        @input="handleSearch"
        placeholder="Digite nome, CNPJ, cidade..."
      />
    </div>

    <div v-if="loading" class="loading">Carregando...</div>
    
    <div v-else class="results">
      <div v-if="operadoras.length === 0" class="no-results">
        Nenhuma operadora encontrada
      </div>
      
      <div v-else>
        <div v-for="operadora in operadoras" :key="operadora.id" class="card">
          <h3>{{ operadora.nome_fantasia || 'Nome não disponível' }}</h3>
          <p><strong>CNPJ:</strong> {{ operadora.cnpj || 'Não informado' }}</p>
          <p><strong>Cidade/UF:</strong> {{ operadora.cidade || 'Não informada' }}/{{ operadora.uf || 'UF' }}</p>
          <p><strong>Telefone:</strong> {{ operadora.telefone || 'Não informado' }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchTerm: '',
      operadoras: [],
      loading: false
    }
  },
  methods: {
    async handleSearch() {
      if (this.searchTerm.length < 3) {
        this.operadoras = [];
        return;
      }

      this.loading = true;
      
      try {
        const response = await axios.get('http://localhost:8000/api/buscar-operadoras/', {
          params: { q: this.searchTerm }
        });
        console.log("Dados recebidos:", response.data);
        this.operadoras = [...response.data.resultados];
      } catch (error) {
        console.error("Erro na busca:", error);
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style>
.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.search-box {
  margin: 20px 0;
}

.search-box input {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: 2px solid #ddd;
  border-radius: 6px;
  box-sizing: border-box;
}

.results {
  margin-top: 20px;
}

.loading {
  text-align: center;
  padding: 20px;
  color: #666;
}

.no-results {
  text-align: center;
  padding: 20px;
  color: #666;
  font-style: italic;
}

.card {
  background: #1d4d96;
  border: 1px solid #1d4d96;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.card h3 {
  margin-top: 0;
  color: #2c3e50;
}

.card p {
  margin: 5px 0;
}
</style>