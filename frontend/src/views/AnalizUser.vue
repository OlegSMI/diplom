<template>
  <div class="about">
    <v-row>
      <v-col md="5" >
        <v-card 
        class="my-8 mx-5 text-left"
        color="white"
        dark
        flat
        max-width="900"
        height="485"
        >
        <v-row>
          <v-col md="6">
            <v-card-text class="py-5 black--text">
              <span style="font-size: 26px;">
                Имя: <br>{{person.name}}
              </span>
            </v-card-text>
            <v-card-text class="py-3 black--text">
              <span style="font-size: 20px;">
                Статус: {{person.status}}
              </span>
            </v-card-text>
            <v-card-text class="py-3 black--text">
              <span style="font-size: 20px;">
                Друзей: {{countFriends}}
              </span> 
            </v-card-text>
          </v-col>
          <v-col md="6">
            <v-card-text>
            <v-avatar
            size="180">
              <v-img :src="person.photo"></v-img>
            </v-avatar>
          </v-card-text>
          </v-col>
        </v-row>
        <v-card-text class="black--text">
          Дополнительная информация:
        </v-card-text>
          
             
        </v-card>
      </v-col>
      <v-col md="7" >
        <v-card
        class="mx-auto text-center mt-5"
        color="white"
        dark
        flat
        max-width="900"
        >
          <v-card-text>
            <h2 class="black--text font-weight-thin ma-2">
              Активность 
            </h2>
            
            <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
              <HeatChart :person="person" class='absolute'/>
            </v-sheet>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="5" >
        <v-card 
        class="ma-5 text-center"
        color="white"
        dark
        flat
        max-width="900"

        >
          <v-card-text>
            <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded >
              <DonutChart class="donut"/>
            </v-sheet>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col md="7" >
        <v-card
        class="mx-auto text-center my-5"
        color="white"
        flat
        dark
        max-width="900"
        >
          <v-card-text>
            <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
              <BestChart class='absolute'/>
            </v-sheet>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="5" >
        <v-card 
        class="ma-5 text-center"
        color="#4282D3"
        dark
        flat
        max-width="900"
        >
          <v-card-text>
            <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
              <RadarChart class='absolute'/>
            </v-sheet>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col md="7" >
        <v-card
        class="mx-auto text-center my-5"
        color="#4282D3"
        dark
        max-width="900"
        >
          <v-card-text>
            <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
              <SparklineChart class='absolute'/>
            </v-sheet>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>


<script>
import SparklineChart from '../components/graphs/SparklinePostsComponent'
import RadarChart from '../components/graphs/RadialGraphPostComponent'
import DonutChart from '../components/graphs/DonutPostsComponent'
import HeatChart from '../components/graphs/HeatMapComponent'
import BestChart from '../components/graphs/TheBestGraph'
export default {
  components: { SparklineChart, RadarChart, DonutChart, HeatChart, BestChart},
  data() {
    return {
      person: [],
      times: [],
    }
  },
  created(){
    this.person = this.$store.getters.getTodoById(Number(this.$route.query.num))
  },
  computed: {
    countFriends: function() {
      return (this.person.friends).length
    },
  }
}
</script>

<style>
.donut {
  text-align: center;
  vertical-align: middle;
  position: relative;
}
</style>
