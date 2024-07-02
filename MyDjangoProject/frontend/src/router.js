// router.js
import { createRouter, createWebHistory } from 'vue-router';
import MangaList from '../src/components/MangaList.vue'; // Nombre ajustado según tus componentes
import ChapterList from '../src/components/ChapterList.vue'; // Nombre ajustado según tus componentes
import PageList from '../src/components/PageList.vue'; // Nombre ajustado según tus componentes

const routes = [
  {
    path: '/mangas',
    name: 'MangaList',
    component: MangaList
  },
  {
    path: '/mangas/:manga_id/chapters',
    name: 'ChapterList',
    component: ChapterList,
    props: true
  },
  {
    path: '/chapters/:chapter_id/pages',
    name: 'PageList',
    component: PageList,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
