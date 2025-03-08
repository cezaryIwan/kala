<template>
<div id="app">
    <multiselect v-model="chosenAsset" :options="listOfAssets" :show-labels="true"></multiselect>
    <input type ="number" v-model="number" class="nb"/>
    <button @click="handleAssetAdd" class="nb">Add</button>
</div>
</template>
<script>
    import Multiselect from 'vue-multiselect'
    import { ref } from 'vue'
    import axios from 'axios'
    export default{
        components: {
            Multiselect,
        },
        setup(){
            const chosenAsset = ref('bronze');
            const listOfAssets = ref(['bronze','silver','gold','platinum','diamond']);
            const balance = ref(null);
            function handleAssetAdd(){
                const newAsset = {
                    type: chosenAsset.value,
                    balance: parseFloat(balance.value)
                }
                    axios.post('http://localhost:8000/asset/add', newAsset)
                    .then(response => {
                        window.alert(`Dodano aktywo: ${response}`);
                    })
                    .catch(error => {
                        window.alert(`Błąd dodawania aktywa: ${error}`);
                    });
                }
            return {chosenAsset, listOfAssets, balance, handleAssetAdd}
    }
}

</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>
.nb{
    height: 40px;
    width: 40px;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
}
.nb::-webkit-inner-spin-button, 
.nb::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>