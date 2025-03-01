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
    export default{
        components: {
            Multiselect,
        },
        setup(){
            const chosenAsset = ref('bronze');
            const listOfAssets = ref(['bronze','silver','gold','platinum','diamond']);
            const balance = ref(null);
            async function handleAssetAdd(){
                const newAsset = {
                    type: value.value,
                    balance: parseFloat(number.value)
                }
                try {
                    const response = await fetch('http://localhost:8000/asset/add', {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(newAsset),
                    });
                } catch (error) {
                    console.error('Error:', error);
                }   
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