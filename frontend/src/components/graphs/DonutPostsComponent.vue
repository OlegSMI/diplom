<template>
    <div id="chart" class="pb-3">
        <apexchart type="donut" height="300" :options="chartOptions" :series="series"></apexchart>
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
            series: [44, 123, 17, 215],
            chartOptions: {
                labels:['Группы (воен)', 'Группы (не воен)', 'Посты (воен)', 'Посты (не воен)'],
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
                }],
                
          },
       }
    }
}
</script>