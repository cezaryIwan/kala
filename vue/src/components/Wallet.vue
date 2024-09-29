<template class="chart">
  <div class="chart">
    <SummaryChart />
  </div>
</template>

<script>
import SummaryChart from "./SummaryChart.vue";
export default {
  name: "Wallet",
  components: {
    SummaryChart,
  },
};
</script>

<style lang="scss">
.chart {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1 0 auto;
}
</style>
