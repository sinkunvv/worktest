<template>
  <v-responsive class="border rounded">
    <v-app>
      <v-app-bar title="WorkSample Test"></v-app-bar>
      <client-only>
        <v-navigation-drawer permanent>
          <v-list>
            <v-list-item title="商品写真"></v-list-item>
          </v-list>
        </v-navigation-drawer>
      </client-only>
      <v-main>
        <slot />
      </v-main>
    </v-app>
  </v-responsive>
</template>