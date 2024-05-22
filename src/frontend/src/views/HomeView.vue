<script setup lang="ts">
import SearchBar from '../components/SearchBar.vue'
import TitleComponent from '../components/TitleComponent.vue'
import FileInput from '../components/FileInput.vue'
</script>

<template>
  <main>
    <div class="md:container md:mx-auto text-center mt-8">
      <TitleComponent />
      <SearchBar />
      <h1>OR</h1>
      <FileInput />
    </div>
  </main>
</template>
