<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card class="pa-6" style="width: 360px;">
      <v-form class="d-flex flex-column gap-4">
        <v-text-field
          class="w-100"
          label="Email"
          v-model="email"
        />
        <v-text-field
          class="w-100"
          label="Password"
          type="password"
          v-model="password"
        />
        <v-btn class="w-100" color="primary" @click="handleLogin">Log in</v-btn>
        <v-btn class="w-100" @click="$router.push('/register')">Register</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">

    definePage({
        meta: {
            hideNavbar: true
        }
    })

    import { ref } from 'vue'
    import axios from 'axios'
    import { useRouter } from 'vue-router'

    const router = useRouter()
    const email = ref('')
    const password = ref('')

    function handleLogin() {
    const params = new URLSearchParams()
    params.append('username', email.value)
    params.append('password', password.value)

    axios.post(`http://localhost:8000/auth/token`, params, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    })
    .then(response => {
        const token = response.data.access_token
        localStorage.setItem('access_token', token)
        router.push('/wallet')
    })
    .catch(error => {
        console.error('Login error:', error.response?.data || error.message)
        showError(error.response?.data?.detail || 'Błąd logowania')
    })
    }
</script>
