<script setup lang="ts">
import type { Images, Menus } from "@/types/images";
interface Emits {
  (e: "setImages", images: Images[]): void;
}
interface Props {
  images: Images[];
}

const props = defineProps<Props>();
const emit = defineEmits<Emits>();

const _images = ref<Images[]>(props.images);

const deleteImage = (index: number) => {
  _images.value.splice(index, 1);
  emit("setImages", _images.value);
}

</script>

<template>
  <v-container>
    <v-row>
      <v-col cols="3" v-for="(image, index) in images" :key="index">
        <v-img class="image-list" :aspect-ratio="1" :src=image.url max-width="500">
          <v-menu location="bottom" :offset="[-35, 85]">
            <template v-slot:activator="{ props }">
              <v-btn class="setting-menu" color="grey-darken-3" v-bind="props">設定</v-btn>
            </template>
            <v-list density="compact">
              <v-list-item>
                <template v-slot:prepend>
                  <v-icon class="mr-n5" icon="mdi-arrow-right-thick"></v-icon>
                </template>
                <v-list-item-title>右に移動</v-list-item-title>
              </v-list-item>
              <v-divider />
              <v-list-item @click="console.log('aaaa')">
                <template v-slot:prepend>
                  <v-icon class="mr-n5" icon="mdi-arrow-left-thick"></v-icon>
                </template>
                <v-list-item-title>左に移動</v-list-item-title>
              </v-list-item>
              <v-divider />
              <v-list-item base-color="red-darken-3" @click="deleteImage(index)">
                <template v-slot:prepend>
                  <v-icon class="mr-n5" icon="mdi-trash-can"></v-icon>
                </template>
                <v-list-item-title>画像を削除</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-img>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.image-list {
  border: 1px solid rgba(0, 0, 0, 0.3);
}

.setting-menu {
  position: absolute;
  opacity: 0.5;
  right: 0;
}
</style>