<template>
    <div id="chart">
        <apexchart type="radar" height="350" :options="chartOptions" :series="series"></apexchart>
      </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
    components: {
      apexchart: VueApexCharts,
    },
    props:{
      data_user: Array
    },
    data: function(){
       return {
           series: [{
            name: 'Series 1',
            data: this.data_user,
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
              categories: ['Посты', 'Число друзей', 'Комментарии', 'Фотографии', 'Число групп', 'Общая активность'],
              floating: false,
              labels: {
                show: true,
                rotateAlways: false,
                style: {
                    colors: ['#dfg534','d1dddd','d1dddd','d1dddd','d1dddd','d1dddd'],
                    fontSize: '12px',
                    fontFamily: 'Arial',
                    fontWeight: 400,
                    cssClass: 'apexcharts-xaxis-label',
                },
                offsetX: 0,
                offsetY: 0,
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
          }
            
          },
       }
    }
}
    
</script>