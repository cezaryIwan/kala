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
        <v-text-field
          class="w-100"
          label="Confirm Password"
          type="password"
          v-model="confirmPassword"
        />
        <v-btn class="w-100" color="primary" @click="handleRegister">Register</v-btn>
        <v-btn class="w-100" @click="$router.push('/login')">Back to Login Page</v-btn>
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
    import axios from 'axios'
    import { useRouter } from 'vue-router'
    const router = useRouter()
    const email = ref('');
    const password = ref('');
    const confirmPassword = ref('');
    function handleRegister (){
        if (password.value !== confirmPassword.value){
            window.alert('Passwords do not match!');
            return;
        }
        if (password.value.length == 0 || email.value.length == 0){
            window.alert('Email and Password cannot be empty!');
            return;
        }
        const newUser = {
            email: email.value,
            password: password.value,
        }
        axios.post('http://localhost:8000/auth/register', newUser, {
            headers: {
            'Content-Type': 'application/json',
            },
        })
            .then(response => {
            window.alert(`Registered user: ${email.value}`);
            router.push('/login');
            })
            .catch(error => {
            window.alert(`Error: ${error.response ? error.response.data : error.message}`);
            });
        }
</script>