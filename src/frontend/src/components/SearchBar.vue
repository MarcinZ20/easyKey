<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { mount, flushPromises } from '@vue/test-utils'

const query = ref('')

function submit(): string {
  axios
    .get('http://localhost:8000/search', {
      params: {
        query: query.value
      }
    })
    .then((response) => {
      console.log(response.data)
    })
    .catch((error) => {
      console.log(error)
    })
  return query.value
}
</script>

<template>
  <div class="md:container md:mx-auto px-3">
    <input
      type="text"
      v-model.lazy="query"
      placeholder="Houdini - Dua Lipa"
      class="input input-bordered input-secondary input-lg w-full max-w-xs mr-2"
    />
    <button v-on:click="submit()" class="btn btn-secondary btn-lg">Search</button>
  </div>
</template>
