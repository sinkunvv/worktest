<script setup lang="ts">
import { ref, onMounted } from "vue"
import type { Images } from "@/types/images";

const images = ref<Images[]>([])
const api_url: string = 'https://httpbin.org/get'

onMounted(async () => {
  await nextTick()
  await getImage()
})

const getImage = async () => await useFetch(api_url).then(res => {
  console.log(res.data.value)
  setImages([])
})

const setImages = (_images: Images[]) => {
  images.value = _images
}
</script>

<template>
  <v-container>
    <image-list :images=images @setImages="setImages" />
    <upload-button :images=images @setImages="setImages" />
    <save-button :images=images />
  </v-container>
</template>