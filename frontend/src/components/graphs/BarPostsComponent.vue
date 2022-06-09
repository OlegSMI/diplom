<template>
   <div>
     <apexcharts height="400" type="bar" :options="chartOptions" :series="series"></apexcharts>
   </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
    components: {
      apexcharts: VueApexCharts,
    },
    props:{
      users:{
        type: Array
      },
      postsUser:{
        type: Array
      }
    },

      data: function() {
      return {
        chartOptions: {
          grid: {
            show: false,  
          },
          chart: {
            id: 'posts',
            animations: {
                enabled: true,
                easing: 'easeinout',
                speed: 800,
                animateGradually: {
                    enabled: false,
                },
                dynamicAnimation: {
                    enabled: true,
                    speed: 350
                }
            },
            toolbar: {
            show: false,
          }
          },
          yaxis: {
            show: false
          },
          xaxis: {
            categories: this.users,
            floating: false,
            labels: {
              show: true,
              rotate: -90,
              rotateAlways: true,
              style: {
                  colors: 'black',
                  fontSize: '12px',
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
          fill: {
          colors: ['#1E90FF'],
          opacity: 1,
          type: 'solid',
          },
          tooltip: {
            enabled: false
          },
          dataLabels: {
            enabled: true,
            textAnchor: 'middle',
            offsetX: 0,
            offsetY: -30,
            style: {
                fontSize: '20px',
                fontFamily: 'Helvetica, Arial, sans-serif',
                fontWeight: 'bold',
                colors: undefined
            },
            background: {
              enabled: true,
              foreColor: 'black',
              opacity: 0,
            },
          },
          plotOptions: {
            bar: {
                // borderRadius: 20,
                dataLabels: {
                    position: 'top',
                },
            }
          },
        },
        series: [{
          name: 'series-1',
          // data: this.postsUser
          data: [7,9,4,7,3,4,2,7,9]
        }],
        
        
      }
    },
};


</script>

<style>
.apexcharts-bar-series.apexcharts-plot-series .apexcharts-series path {
clip-path: inset(5% 5% 5% 0% round 20px);
}</style>



