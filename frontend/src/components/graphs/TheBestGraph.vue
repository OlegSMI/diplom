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
    data: function(){
       return {
           series: [{
            name: 'Выявленые пользователи',
            type: 'column',
            data: [4, 3, 6, 7, 5, 2, 2, 0, 0, 2, 1, 4]
          }, {
            name: 'Выявленные действия',
            type: 'line',
            data: [12, 5, 11, 22, 4, 5, 6, 0, 0, 2, 2, 6]
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
            labels: ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сент', 'Окт', 'Нояб', 'Дек'],
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