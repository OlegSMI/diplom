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
    props:{
      posts:{
        type: Array
      }
    },
    created(){
      for (var i in this.posts){
        this.users.push(this.posts[i].name)
        this.postsUser.push(this.posts[i].posts.length) 
        console.log(this.users)
        console.log(this.postsUser)
      }
    },
    computed:{
      getUser(){
        for (var i in this.posts){
          this.users.push(this.posts[i].name)
        }
        return this.users
      },
      getPosts(){
        for (var i in this.posts){
          this.postsUser.push(this.posts[i].posts.length) 
        }
        return this.postsUser
      }
    },
    methods:{
      changeData() {
        VueApexCharts.exec('posts', "updateOptions", {
          xaxis: {
            categories: this.getUser
          }
        });
        VueApexCharts.exec('posts', "updateSeries", [
          {
            data: this.getPosts
          }
        ]);
      }
    },
    data: function() {
      return {
        users: [],
        postsUser: [],
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
            categories: [],
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
          data: []
        }],
        
        
      }
    },
};


</script>

<style>
.apexcharts-bar-series.apexcharts-plot-series .apexcharts-series path {
clip-path: inset(5% 5% 5% 0% round 20px);
}</style>



