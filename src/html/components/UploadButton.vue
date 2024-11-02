<script setup lang="ts">
import { ref } from "vue";
import type { Images } from "@/types/images";

interface Emits {
  (e: "setImages", images: Images[]): void;
}

interface Props {
  images: Images[];
}

const props = defineProps<Props>();
const emit = defineEmits<Emits>();

const uploadInput = ref<HTMLInputElement>();
const _images = ref<Images[]>(props.images);

/**
 * Input File Wrapper
 */
const triggerInput = () => {
  uploadInput.value?.click();
};

/**
 * 仮アップロード
 * @param event HTMLInput
 */
const preUpload = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const files = target.files;
  let position: number = _images.value.length
  if (files) {
    Array.from(files).map((file: File, index: number) => (
      _images.value.push({
        url: URL.createObjectURL(file),
        name: file.name,
        position: position++,
        file: file,
      }))
    );
    emit("setImages", _images.value);
    target.value = ""
  }
};
</script>

<template>
  <div>
    <v-btn color="grey-lighten-1" prepend-icon="mdi-folder-open-outline" @click="triggerInput">ファイルを選択する
    </v-btn>
    <input ref="uploadInput" type="file" multiple accept="image/*" style="display: none" @change="preUpload" />
  </div>
</template>