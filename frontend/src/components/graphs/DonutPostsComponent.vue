<template>
    <div id="chart" class="pa-5">
        <apexchart type="donut" height="500" :options="chartOptions" :series="series"></apexchart>
      </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
    components: {
      apexchart: VueApexCharts,
    },
    data: function(){
       return {
           series: [44, 55, 41, 17, 15],
            chartOptions: {
                chart: {
                type: 'donut',
                },
                responsive: [{
                breakpoint: 480,
                options: {
                    chart: {
                    width: 200
                    },
                    legend: {
                    position: 'bottom'
                    }
                }
                }]
          },
       }
    }
}
</script>