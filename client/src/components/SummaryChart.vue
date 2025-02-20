<template>
    <div id="chart">
    <DoughnutChart :chartData="testData" />
  </div>
</template>
<script>
import { defineComponent } from 'vue'
import { DoughnutChart } from 'vue-chart-3'
import { Chart, registerables } from "chart.js"
Chart.register(...registerables)

export default defineComponent ({
  data(){
    return{
      assets: [],
      testData:{
        labels: [],
        datasets:[
          {
            data: [],
            backgroundColor: ['#77CEFF', '#0079AF', '#123E6B', '#97B0C4', '#A5C8ED'],
          },
        ]
      },
    };
  },
  created() {
    this.fetchAssets();
  },
  methods:{
    async fetchAssets(){
      try{
        const response = await fetch("http://localhost:8000/wallet")
        const data = await response.json();
        console.log(data);
        this.assets = data;
        
        this.testData.labels = this.assets.map(asset=>asset.type);
        this.testData.datasets[0].data = this.assets.map(asset=>asset.balance);

        console.log(this.testData);
      } catch (error){
        console.error(error);
      }
    },
  },
  name: "SummaryChart",
  components : {
    DoughnutChart
  },
  setup() {
    return {};
  },
});
</script>
<style lang="scss">
  
  chart {
    position: center;
  }
</style>
