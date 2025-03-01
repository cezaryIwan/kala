<template>
<div id="app">
    <multiselect v-model="value" :options="options" :show-labels="true"></multiselect>
    <input type ="number" v-model="number" class="nb"/>
    <button @click="handleButtonClick" class="nb">Add</button>
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
            const value = ref('');
            const options = ref(['bronze','silver','gold','platinum','diamond']);
            
            const number = ref(null);

            
            async function handleButtonClick(){
                const newAsset = {
                    type: value.value,
                    balance: parseFloat(number.value)
                };
                console.log(newAsset);
                try {
                    const response = await fetch('http://localhost:8000/asset/add', {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(newAsset),
                    });
                    if (response.ok) {
                        const data = await response.json();
                        console.log('Response:', data);  // Logowanie odpowiedzi
                    } else {
                        console.error('HTTP Error:', response.status);  // Wykrywanie błędów HTTP
                    }
                } catch (error) {
                    console.error('Error:', error);
                }
            }
            return {value, options, number, handleButtonClick}
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