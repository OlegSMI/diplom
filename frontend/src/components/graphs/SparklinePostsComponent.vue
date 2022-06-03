<template>
  <div class="example ma-5">
    <apexchart height="500" type="area" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  name: 'AreaExample',
  components: {
      apexchart: VueApexCharts,
    },
  data: function() {
    return {
      chartOptions: {
        grid: {
        show: false,  
        },
        dataLabels: {
            enabled: false,
        },
        yaxis: {
            show: false
        },
        xaxis: {
            categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
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
            enabled: false,
        },
        fill: {
          colors: ['#FFFFFF'],
          gradient: {
            shade: 'dark',
            type: "vertical",
            shadeIntensity: 0.5,
            gradientToColors: undefined,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 1,
            // stops: [0,10,20,30,40,50,60,70,80,90,100],
            colorStops: []
        },
        },
            
        chart: {
            toolbar: {
            show: false,
          },
          

        },
      },
      series: [{
          name: 'series1',
          color: '#FFFFFF',
          data: [31, 40, 28, 51, 42, 109, 100]
      }],
    }
  },
}
</script>