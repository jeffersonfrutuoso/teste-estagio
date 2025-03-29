<script setup>
import { ref } from 'vue'

const termoBusca = ref('')
const operadoras = ref([])
const carregando = ref(false)

const buscarOperadoras = async () => {
  if (termoBusca.value.length < 3) {
    operadoras.value = []
    return
  }
  
  carregando.value = true
  try {
    const response = await fetch(`http://localhost:5000/api/operadoras?q=${encodeURIComponent(termoBusca.value)}`)
    operadoras.value = await response.json()
    console.log("Dados recebidos:", operadoras.value)
  } catch (error) {
    console.error('Erro na busca:', error)
  } finally {
    carregando.value = false
  }
}
</script>

<template>
  <div class="container">
    <h1>Busca de Operadoras ANS</h1>
    
    <input
      v-model="termoBusca"
      @input="buscarOperadoras"
      placeholder="Digite nome ou razão social"
      class="search-input"
    >

    <div v-if="carregando" class="loading">Carregando...</div>

    <div v-if="operadoras.length > 0" class="results">
      <table>
        <thead>
          <tr>
            <th>Registro ANS</th>
            <th>Nome Fantasia</th>
            <th>Razão Social</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="op in operadoras" :key="op['Registro ANS']">
            <td>{{ op['Registro_ANS'] }}</td>
            <td>{{ op['Nome_Fantasia'] || 'N/A' }}</td>
            <td>{{ op['Razao_Social'] }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else-if="termoBusca && !carregando" class="no-results">
      Nenhuma operadora encontrada
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.search-input {
  width: 100%;
  padding: 0.75rem;
  margin-bottom: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.loading {
  color: #666;
  padding: 1rem;
  text-align: center;
}

.no-results {
  color: #888;
  padding: 1rem;
  text-align: center;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

th, td {
  border: 1px solid #ddd;
  padding: 0.75rem;
  text-align: left;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

tr:hover {
  background-color: #f0f0f0;
}
</style>