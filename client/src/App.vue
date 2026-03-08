<template>
  <v-app>
    <v-main v-if="isReady">
      <Navbar v-if="!$route.meta.hideNavbar" />
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const isReady = ref(false)
const router = useRouter()

onMounted(async () => {
  await router.isReady()
  isReady.value = true
})
</script>
