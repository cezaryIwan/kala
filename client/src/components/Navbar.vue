<template>
  <v-container>
    <v-navigation-drawer>
      <v-list-item linkt subtitle="Vuetify" title="My Application" to="/" />
      <v-divider />
      <v-list-item link title="Wallet" to="/wallet" />
      <v-list-item link title="Add Asset" to="/assetadd" />
      <v-list-item>
        <v-btn variant="text" @click="logout">Log out</v-btn>
      </v-list-item>

    </v-navigation-drawer>
  </v-container>
</template>
<script setup>
  import { useRouter } from 'vue-router'

  const router = useRouter()

  function logout() {
    localStorage.removeItem('access_token')
    router.push('/login')
  }
</script>
