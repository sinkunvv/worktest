<script setup lang="ts">
import { ref } from "vue"
import type { Images } from "@/types/images";

const images = ref<Images[]>([])

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