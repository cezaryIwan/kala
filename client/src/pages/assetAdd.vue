<template>
    <v-app-bar>
        <v-container class="d-flex justify-space-between">
            <a href="#"> Akcje </a>
            <a href="#"> Obligacje </a>
            <a href="#"> Surowce </a>
        </v-container>
    </v-app-bar>
    <v-container class="d-flex flex-row align-center justify-center">
        <SummaryChart/>
        <v-container class="d-flex flex-column align-center justify-center w-50 mx-0" style="min-height: calc(80vh - 64px);">
            <v-container class="d-flex flex-column ">
                <v-select
                v-model="chosenAsset"
                label="Select"
                :items="listOfAssets"
                ></v-select>
                <v-number-input
                v-model="balance"
                    :reverse="false"
                    controlVariant="default"
                    label="Balance"
                    :precision="2"
                    :min="0"
                    :default="0.00"></v-number-input>
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
    export default{
        setup(){
            const chosenAsset = ref('bronze');
            const listOfAssets = ref(['bronze','silver','gold','platinum','diamond']);
            const balance = ref(null);
            function handleAssetAdd(){
                const newAsset = {
                    type: chosenAsset.value,
                    balance: parseFloat(balance.value)
                }
                    axios.post('http://localhost:8000/asset/add', newAsset, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(response => {
                        window.alert(`Dodano aktywo: ${chosenAsset.value} o wartości ${balance.value}`);
                        window.location.reload();
                    })
                    .catch(error => {
                        window.alert(`Błąd: ${error.response ? error.response.data : error.message}`);
                    });
                }
            return {chosenAsset, listOfAssets, balance, handleAssetAdd}
    }
}

</script>

<style>


</style>

