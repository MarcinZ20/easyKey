<script setup lang="ts">
import { ref } from 'vue'

const title = ref('')

function submit(): string {
  return 'Here is ' + title
}
</script>

<template>
  <div class="md:container md:mx-auto px-3">
    <input
      type="text"
      v-model.lazy="title"
      placeholder="Houdini - Dua Lipa"
      class="input input-bordered input-secondary input-lg w-full max-w-xs mr-2"
    />
    <button v-on:click="submit()" class="btn btn-secondary btn-lg">Search</button>
  </div>
</template>
