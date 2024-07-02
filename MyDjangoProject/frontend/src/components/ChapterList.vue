<!-- ChapterList.vue -->
<template>
  <div>
    <h1>Capítulos de {{ mangaTitle }}</h1>
    <ul>
      <li v-for="chapter in chapters" :key="chapter.ChapterId">
        <router-link :to="'/mangas/' + mangaId + '/chapters/' + chapter.ChapterId">{{ chapter.Title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import apiClient from '@/axios';

export default {
  data() {
    return {
      chapters: [],
      mangaId: this.$route.params.manga_id,
      mangaTitle: '',
    };
  },
  created() {
    this.fetchChapters();
    this.fetchMangaTitle();
  },
  methods: {
    fetchChapters() {
      apiClient.get(`mangas/${this.mangaId}/chapters/`)
        .then(response => {
          this.chapters = response.data;
        })
        .catch(error => {
          console.error('Error fetching chapters', error);
        });
    },
    fetchMangaTitle() {
      apiClient.get(`mangas/${this.mangaId}/`)
        .then(response => {
          this.mangaTitle = response.data.Title;
        })
        .catch(error => {
          console.error('Error fetching manga title', error);
        });
    },
  },
};
</script>

<style scoped>
/* Estilos específicos del componente */
</style>
