<template>
   <div>
     <apexcharts height="500" type="bar" :options="chartOptions" :series="series"></apexcharts>
   </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'


export default {
    components: {
      apexcharts: VueApexCharts,
    },
    data: function() {
      return {
        chartOptions: {
          grid: {
            show: false,  
          },
          // colors: 'white',
          chart: {
            id: 'vuechart-example',
            toolbar: {
            show: false,
            tools: {
              download: false,
              selection: false,
              zoom: false,
              zoomin: false,
              zoomout: false,
              pan: false,
              reset: false,
            },
          }
          },
          yaxis: {
            show: false
          },
          xaxis: {
            categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
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
          tooltip: {
            enabled: false
          },
  
          
        },
        
        series: [{
          name: 'series-1',
          data: [30, 40, 45, 50, 49, 60, 70, 91]
        }],
        
      }
    },
};
</script>



