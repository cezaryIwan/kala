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

<script setup>

    definePage({
        meta: {
            hideNavbar: true
        }
    })
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    import { login } from '@/services/authService.js'

    const router = useRouter()
    const email = ref('')
    const password = ref('')

    const handleLogin = async () => {
  try {
    await login(email.value, password.value)
    router.push('/wallet')
  } catch (error) {
    alert(error.response?.data?.detail || 'Błąd logowania')
  }
}
</script>
