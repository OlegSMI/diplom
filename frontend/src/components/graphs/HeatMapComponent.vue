<template>
    <div id="chart" >
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
            data: this.generateData(12, {
              min: 0,
              max: 1
            })
          },
          {
            name: 'Вт',
            data: this.generateData(12, {
              min: 0,
              max: 4
            })
          },
          {
            name: 'Ср',
            data: this.generateData(12, {
              min: 0,
              max: 2
            })
          },
          {
            name: 'Чт',
            data: this.generateData(12, {
              min: 0,
              max: 3
            })
          },
          {
            name: 'Пт',
            data: this.generateData(12, {
              min: 0,
              max: 1
            })
          },
          {
            name: 'Сб',
            data: this.generateData(12, {
              min: 0,
              max: 2
            })
          },
          {
            name: 'Вс',
            data: this.generateData(12, {
              min: 0,
              max: 4
            })
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
              enabled: true
            },
            colors: ["#008FFB"],
            xaxis: {
            // type: 'datetime',
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
    generateData(count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {
        var x = (i + 1).toString();
        var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
        series.push({
          x: x,
          y: y
        });
        i++;
      }
      return series;
    }
    }
}
</script>