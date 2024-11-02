<script setup lang="ts">
import type { Images } from "@/types/images";

interface Props {
    images: Images[];
}

const props = defineProps<Props>();
const saved = ref<boolean>(false)
const api_url = ref<string>('https://httpbin.org/json')

</script>
<template>
    <div class="text-center mt-3">
        <v-btn class="save-button" variant="flat" color="secondary" @click="saved = true">
            保存
        </v-btn>
        <v-snackbar location="top" v-model="saved" timeout="3000">
            データを保存しました
        </v-snackbar>
    </div>
</template>

<style scoped>
.save-button {
    padding: 0 20vw;
}

</style>