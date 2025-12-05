<template>
  <v-app-bar>
    <v-container fluid>
      <v-row class="align-center" no-gutters>
        <v-spacer />
        <v-list-item class="rounded-lg" link>Akcje</v-list-item>
        <v-spacer />
        <v-list-item class="rounded-lg" link>Obligacje</v-list-item>
        <v-spacer />
        <v-list-item class="rounded-lg" link>Surowce</v-list-item>
        <v-spacer />
      </v-row>
    </v-container>
  </v-app-bar>
  <v-container class="d-flex flex-row align-center justify-center">
    <SummaryChart />
    <v-container class="d-flex flex-column align-center justify-center w-50 mx-0" style="min-height: calc(80vh - 64px);">
      <v-container class="d-flex flex-column ">
        <v-select
          v-model="chosenAsset"
          :items="listOfAssets"
          label="Select"
        />
        <v-number-input
          v-model="balance"
          control-variant="default"
          :default="0.00"
          label="Balance"
          :min="0"
          :precision="2"
          :reverse="false"
        />
      </v-container>
      <v-container class="d-flex justify-end">
        <v-btn @click="handleAssetAdd"> Dodaj </v-btn>
      </v-container>
    </v-container>
  </v-container>

</template>
<script>
  import { ref } from 'vue'
  import axios from 'axios'
  import { assets } from '../utilities/properties.js'
  export default{
    setup (){
      const chosenAsset = ref('bronze');
      const listOfAssets = ref(assets);
      const balance = ref(null);
      function handleAssetAdd (){
        const token = localStorage.getItem('access_token');
        const newAsset = {
          type: chosenAsset.value,
          balance: parseFloat(balance.value),
        }
        axios.post('http://localhost:8000/asset/add', newAsset, {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`
          },
        })
          .then(response => {
            window.alert(`Dodano aktywo: ${chosenAsset.value} o wartości ${balance.value}`);
            window.location.reload();
          })
          .catch(error => {
            window.alert(`Błąd: ${error.response ? error.response.data : error.message}`);
          });
      }
      return { chosenAsset, listOfAssets, balance, handleAssetAdd }
    },
  }
</script>

<style>


</style>
