<!-- MangaList.vue -->
<template>
  <div class="manga-list">
    <h1>Mangas Disponibles</h1>
    <ul>
      <li v-for="manga in mangas" :key="manga.MangaId">
        <router-link :to="'/mangas/' + manga.MangaId">{{ manga.Title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import apiClient from '@/axios';

export default {
  data() {
    return {
      mangas: [],
    };
  },
  created() {
    this.fetchMangas();
  },
  methods: {
    fetchMangas() {
      apiClient.get('mangas/')
        .then(response => {
          this.mangas = response.data;
        })
        .catch(error => {
          console.error('Error fetching mangas', error);
        });
    },
  },
};
</script>

<style scoped>
/* Estilos específicos del componente */
.manga-list {
  max-width: 600px;
  margin: 0 auto;
}
</style>
