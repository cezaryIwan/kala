<template>
  <div id="chart">
    <DoughnutChart :chartData="doughnutChartData" />
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
    const doughnutChartData = reactive({
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
        doughnutChartData.labels = data.map((asset)=>asset.type);
        doughnutChartData.datasets[0].data = data.map((asset)=>asset.balance);
      } catch (error){
        console.error(error);
      }
    }
    fetchAssets();
    return {doughnutChartData};
  },
});
</script>
<style lang="scss">
  
  chart {
    position: center;
  }
</style>
