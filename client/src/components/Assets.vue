<template>
    <div class="assets">
        <div class="assetsHeader">
            <a href="#"> Akcje </a>
            <a href="#"> Obligacje </a>
            <a href="#"> Surowce </a>
        </div>
        <div class = "assetsContent">
            <div class = "assetsInputs">
                <div class="wrapper">
                    <div class="inputDecorator">
                        <label for="balanceInput">Balans</label>
                        <input type ="number" v-model="balance" class="nb" id="balanceInput" placeholder="Balans"/>
                        
                    </div>
                    <div class="supporting-text"> Tekst pomocniczy dla balans</div>  
                    <div class="tooltip">
                        <a class="tooltipIcon"> ? </a>
                        <span class="tooltipText">Tooltip dla balans</span>
                    </div>    
                </div>     
            <multiselect v-model="chosenAsset" :options="listOfAssets" :show-labels="true" :selectLabel="null" :selectedLabel="null" :deselectLabel="null" :allow-empty="false" :placeholder="chosenAsset"></multiselect>
            </div>
            <div class="assetsButtons">
                <button id="cancel"> Anuluj </button>
                <button @click="handleAssetAdd" id="apply">Zatwierdź</button>
            </div>
        </div>
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
                    axios.post('http://localhost:8000/asset/add', newAsset, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(response => {
                        window.alert(`Dodano aktywo: ${chosenAsset.value} o wartości ${balance.value}`);
                    })
                    .catch(error => {
                        window.alert(`Błąd: ${error.response ? error.response.data : error.message}`);
                    });
                }
            return {chosenAsset, listOfAssets, balance, handleAssetAdd}
    }
}

</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>

.assets{
    display: flex;
    flex-direction: column;
    width: 100vw;
    height: 100vh;
}
.assetsHeader{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items:center;
    background-color:bisque;
    padding: 20px 220px;
        @media screen and (max-width: 1024px) {
        padding: 20px 100px;      
    }
}
.assetsHeader a{
  color:brown;
  text-decoration: none;
}
.assetsContent{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 90vh;
}
.assetsInputs{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 210px;
    margin: 20px;
}
.wrapper{
    display: flex;
    flex-direction: column;
    
    width:210px;
    margin: 20px;
}
.assetsInputs input{
    font-size: 30px;
}
.tooltip{
    position: relative;
    display: inline-block;
    cursor: pointer;
}
.tooltipText{
    visibility:hidden;
    transform: translateY(-50%);
    margin-left: 2px;
}
.tooltipIcon:hover .tooltipText{
    visibility:visible;
    opacity: 1;
}
.inputDecorator{
    height: 56px;
    width: 210px;
    padding: 5px;
    border: 1px solid #ccc;
    background-color: rgb(230, 224, 233);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    border-radius: 5px;
}

.multiselect{
    width:210px;
    height:56px;
}
.multiselect__single{
    font-size:30px;
}
.multiselect__tags{
    height:56px;
    display:flex;
    align-items:center;
}
.assetsButtons{
    width:30vw;
    display: flex;
    justify-content:center;
}
.assetsButtons button{
    margin: 0 10px;
}
.supporting-text{
    color:grey;
    font-size: 12px;
    margin-top: 5px;
    margin-left: 5px;
}
.nb{
    background-color: transparent;
    border: none;
    width: 200px;
    height: 31px;
}
.nb::-webkit-outer-spin-button,
.nb::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
label{
    color:dimgrey;
    width: 210px;
    height: 20px;
}
.assetsButtons button{
    padding: 5px 10px;
    height: 40px;
    border-radius: 5px;
    font-size: 20px;
}
#apply{
    color:white;
    background-color: black;
}
#cancel{
    color:black;
    background-color: white; 
}
</style>