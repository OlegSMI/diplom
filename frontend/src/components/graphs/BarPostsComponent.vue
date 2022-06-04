<template>
   <div>
     <apexcharts height="500" type="bar" :options="chartOptions" :series="series"></apexcharts>
   </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  created(){
        this.$store.dispatch('loadItems')
        
        if(this.$store.getters.getState===true){
          if(this.$store.getters.getCount===0){
            setTimeout(this.theOneFunc, 8 * 1000, 8);
            this.parseicon = true;
            this.tasks = this.$store.getters.getItems
            this.$store.dispatch('setCount', 1)
            console.log(this.$store.getters.getCount)
          }
          else{
            this.parseicon = false;
            this.tasks = this.$store.getters.getItems
          }
          
        }
      },
    nethods: {
      theOneFunc(){
        this.parseicon = false
      },
    },
    components: {
      apexcharts: VueApexCharts,
    },
    data: function() {
      return {
        chartOptions: {
          grid: {
            show: false,  
          },
          chart: {
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
            id: 'vuechart-example',
            toolbar: {
            show: false,
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
          fill: {
          colors: ['#FFFFFF'],
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
              foreColor: '#fff',
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
          data: [30, 40, 45, 50, 49, 60, 70, 91]
        }],
        
        
      }
    },
};
</script>

<style>
.apexcharts-bar-series.apexcharts-plot-series .apexcharts-series path {
clip-path: inset(5% 5% 5% 0% round 20px);
}</style>



