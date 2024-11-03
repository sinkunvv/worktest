<script setup lang="ts">
import type { Images } from "@/types/images";

interface Props {
    images: Images[];
}

const props = defineProps<Props>();
const saved = ref<boolean>(false)
const api_url = ref<string>('https://httpbin.org/post')

const storeImages = async () => {
    try {
        if (!props.images.length) return
        const formData = new FormData();
        props.images.map((image, index) => {
            formData.append(`images[${index}][url]`, image.url);
            formData.append(`images[${index}][name]`, image.name);
            formData.append(`images[${index}][position]`, image.position.toString());
            formData.append(`images[${index}][file]`, image.file);
        });

        const response = await useFetch(api_url, {
            method: 'POST',
            body: formData,
        });
        console.log(response.data.value)
        saved.value = true;
    } catch (error) {
        console.error(error);
        throw error;
    }
};

</script>
<template>
    <div class="text-center mt-3">
        <v-btn class="save-button" variant="flat" color="secondary" @click="storeImages">
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