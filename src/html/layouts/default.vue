<template>
  <v-layout class="rounded rounded-md">
    <v-app-bar title="WorkSample Test"></v-app-bar>

    <v-navigation-drawer permanent>
      <v-list>
        <v-list-item title="商品写真"></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
      <slot />
    </v-main>
  </v-layout>
</template>