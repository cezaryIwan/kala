<template>
  <div id="chart">
    <DoughnutChart :chartData="testData" />
  </div>
</template>
<script>

import { defineComponent, ref, reactive } from 'vue'
import { DoughnutChart } from 'vue-chart-3'
import { Chart, registerables } from "chart.js"
Chart.register(...registerables)

export default defineComponent ({
  name: "SummaryChart",
  components : {
    DoughnutChart
  },
  setup() {
    const assets = ref([]);
    const testData = reactive({
      labels:[],
      datasets: [
        {
          data: [],
          backgroundColor: ['#77CEFF', '#0079AF', '#123E6B', '#97B0C4', '#A5C8ED'],
        },
      ],
    });
    async function fetchAssets(){
      try{
        const response = await fetch("http://localhost:8000/wallet")
        const data = await response.json();
        assets.value = data;
        testData.labels = assets.value.map((asset)=>asset.type);
        testData.datasets[0].data = assets.value.map((asset)=>asset.balance);
      } catch (error){
        console.error(error);
      }
    }
    fetchAssets();
    console.log(testData);
    return {testData};
  },
});
</script>
<style lang="scss">
  
  chart {
    position: center;
  }
</style>
