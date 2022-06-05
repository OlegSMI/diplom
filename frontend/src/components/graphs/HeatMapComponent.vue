<template>
    <div id="chart" class="ma-5">
      {{person.posts}}
        <apexchart type="heatmap" height="400" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>


<script>
import VueApexCharts from 'vue-apexcharts'
export default {
    components: {
      apexchart: VueApexCharts,
    },
    props: {
      person: {
        type: Object
      }
    },
    data: function(){
       return {
          series: [{
            name: 'Пн',
            data: this.generateData(12, 1)
          },
          {
            name: 'Вт',
            data: this.generateData(12, 2)
          },
          {
            name: 'Ср',
            data: this.generateData(12, 3)
          },
          {
            name: 'Чт',
            data: this.generateData(12, 4)
          },
          {
            name: 'Пт',
            data: this.generateData(12, 5)
          },
          {
            name: 'Сб',
            data: this.generateData(12, 6)
          },
          {
            name: 'Вс',
            data: this.generateData(12, 7)
          },
          ],
          chartOptions: {
            chart: {
              height: 350,
              type: 'heatmap',
              toolbar: {
                show: false,
              },
            },
            dataLabels: {
              enabled: false
            },
            colors: ["#008FFB"],
            xaxis: {
            categories: ['00:00', '02:00', '04:00', '06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
            floating: false,
            labels: {
              show: true,
              rotateAlways: false,
              style: {
                  colors: 'black',
                  fontSize: '14px',
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
          yaxis: {
             labels: {
                show: true,
                align: 'right',
                minWidth: 0,
                maxWidth: 160,
                style: {
                    colors: [],
                    fontSize: '18px',
                    fontFamily: 'Helvetica, Arial, sans-serif',
                    fontWeight: 400,
                    cssClass: 'apexcharts-yaxis-label',
                },
            },
          },
          },
       }
    },
    methods: {
    // generateData(nums, week) {
    //   var series = [];
    //   var first = 0;
    //   var second = 2;
    //   for (var i = 1; i <= nums; i++){
    //     var count = 0;
    //     for (var item in this.person.posts){
    //     if (Number(item.weekday_post) === week && Date(item.timepost) < second && Date(item.timepost) > first){
    //       count++
    //     }
    //   }
    //   series.push({
    //       x: i,
    //       y: count
    //   })
    //   first += 2;
    //   second +=2;
    //   }
    //   return series;
    // }
    }
}
</script>