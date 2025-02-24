<template>
  <div id="chart">
    <DoughnutChart :chartData="doughnutChartData" :options="doughnutChartOptions" />
  </div>
</template>
<script>

import { defineComponent, reactive } from 'vue'
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

    const doughnutChartOptions = reactive({
      plugins: {
        tooltip: {
          enabled: true,
          callbacks: {
            label: function(tooltipItem){
              const label = doughnutChartData.labels[tooltipItem.dataIndex];
              const value = doughnutChartData.datasets[0].data[tooltipItem.dataIndex];
              const sum = doughnutChartData.datasets[0].data.reduce((acc,current)=>acc+current,0);
              const percentage = (value/sum * 100).toFixed(2);
              return `${label}: ${value} (${percentage}%) `;
            },
          },
        },
      },
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
    return {doughnutChartData, doughnutChartOptions};
  },
});
</script>
<style lang="scss">
  
  chart {
    position: center;
  }
</style>
