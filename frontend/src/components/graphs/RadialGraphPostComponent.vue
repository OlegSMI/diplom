<template>
    <div id="chart">
        <apexchart type="radar" height="400" :options="chartOptions" :series="series"></apexchart>
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
           series: [{
            name: 'Series 1',
            data: [80, 50, 30, 40, 100, 20],
          }],
          chartOptions: {
            chart: {
              height: 350,
              type: 'radar',
              toolbar: {
                show: false,
              }
            },
            tooltip: {
            enabled: false,
        },
            xaxis: {
              categories: ['January', 'February', 'March', 'April', 'May', 'June'],
              floating: false,
              labels: {
                show: true,
                rotateAlways: false,
                style: {
                    colors: 'white',
                    fontSize: '20px',
                    fontFamily: 'Arial',
                    fontWeight: 400,
                    cssClass: 'apexcharts-xaxis-label',
                },
                offsetX: 0,
                offsetY: 5,
              },  
              axisBorder: {
                  show: false,
              },
              axisTicks: {
                  show: false,
              },
            },
            
          },
       }
    }
}
    
</script>