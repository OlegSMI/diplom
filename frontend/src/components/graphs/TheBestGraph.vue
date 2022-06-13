<template>
    <div id="chart">
        <apexchart type="line" height="350" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
    components: {
      apexchart: VueApexCharts,
    },
    props:{
      content: Array,
      users: Array,
    },
    data: function(){
       return {
           series: [{
            name: 'Выявленые пользователи',
            type: 'column',
            data: this.users
          }, {
            name: 'Выявленные действия',
            type: 'line',
            data: this.content
          }],
          chartOptions: {
            chart: {
              height: 350,
              type: 'line',
              toolbar:{
                  show: false
              }
            },
            stroke: {
              width: [0, 4]
            },
            dataLabels: {
              enabled: true,
              enabledOnSeries: [1]
            },
            labels: ['00:00', '02:00', '04:00', '06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
            // xaxis: {
            //   type: 'datetime'
            // },
            yaxis: [{
            
            }, {
              opposite: true,
            }],
            tooltip: {
                enabled: true,
                enabledOnSeries: undefined,
                shared: true,
                followCursor: false,
                intersect: false,
                inverseOrder: false,
                custom: undefined,
                fillSeriesColor: false,
                theme: true,
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
          },
       }
    }
}
</script>

<style>
.apexcharts-tooltip {
    background: #f3f3f3;
    color: black;
  }
</style>