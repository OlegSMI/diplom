<template>
  <div class="example">
    <apexchart height="300" type="area" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  name: 'AreaExample',
  components: {
      apexchart: VueApexCharts,
  },
  props:{
    user_active: Array
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
            categories: ["00:00", "02:00", "04:00", "06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"],
            floating: false,
            labels: {
              datetimeFormatter: {
                hour: 'HH:mm'
              },
              show: true,
              rotateAlways: false,
              style: {
                  colors: 'black',
                  fontSize: '12px',
                  fontFamily: 'Arial',
                  fontWeight: 400,
                  cssClass: 'apexcharts-xaxis-label',
              },
              offsetX: 2,
              offsetY: 0,
            },  
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
        },
        tooltip: {
          enabled: true,
          enabledOnSeries: undefined,
          shared: true,
          followCursor: false,
          intersect: false,
          inverseOrder: false,
          custom: undefined,
          fillSeriesColor: false,
          theme: false,
          style: {
            fontSize: '12px',
            fontFamily: undefined
          },
          onDatasetHover: {
              highlightDataSeries: false,
          },
          x: {
              show: false,
          },
          y: {
              show: true
          },
          z: {
              formatter: undefined,
              title: 'Size: '
          },
          marker: {
              show: true,
          },
          fixed: {
              enabled: false,
              position: 'topRight',
              offsetX: 0,
              offsetY: 0,
          },
      },
        fill: {
          colors: ['#1E90FF'],
          gradient: {
            shade: 'dark',
            type: "vertical",
            shadeIntensity: 0.5,
            gradientToColors: undefined,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 1,
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
          name: '',
          color: '#1E90FF',
          data: this.user_active
      }],
    }
  },
}
</script>