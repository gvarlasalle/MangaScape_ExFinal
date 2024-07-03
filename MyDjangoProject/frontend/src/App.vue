<template>
  <div id="app">
    <header>
      <router-link to="/mangas">Mangas</router-link>
    </header>
    
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
/* Estilos globales de la aplicación */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background-color: #6666;
  padding: 10px;
}

header a {
  color: white;
  text-decoration: none;
  margin-right: 10px;
}

header a:hover {
  text-decoration: underline;
}
</style>
