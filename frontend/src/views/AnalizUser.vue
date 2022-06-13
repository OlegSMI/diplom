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
                {{person.first_name}} {{person.last_name}}
              </span>
            </v-card-text>
            <v-card-text class="py-3 black--text">
              <span style="font-size: 20px;">
                Возраст: {{person.age}}
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
              <v-img :src="person.img"></v-img>
            </v-avatar>
          </v-card-text>
          </v-col>
        </v-row>
        <v-card-text class="black--text">
          Дополнительная информация:
          <br>
          <span>
            Число комментариев: {{countComments}}
          </span>
          <br>
          <span>
            Число постов: {{countPosts}}
          </span>
          <br>
          <span>
            Социальная сеть: TestNet
          </span>
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
              Недельная ктивность 
            </h2>
              <HeatChart :person="person" class='absolute'/>
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
            <h2 class="black--text font-weight-thin ma-2">
              Сравнение с другими пользователями
            </h2>
              <RadarChart :data_user="data_user" class="donut"/>
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
              <h2 class="black--text font-weight-thin ma-2">
                Годовая активность
              </h2>
              <BestChart class='absolute'/>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>


<script>
import RadarChart from '../components/graphs/RadialGraphPostComponent'
import HeatChart from '../components/graphs/HeatMapComponent'
import BestChart from '../components/graphs/TheBestGraphUser'
export default {
  components: {RadarChart, HeatChart, BestChart},
  data() {
    return {
      person: [],
      times: [],
      data_user:[]
    }
  },
  created(){
    this.person = this.$store.getters.getTodoById(Number(this.$route.query.num))
    console.log(this.person)
    console.log(this.countPosts)
    console.log(this.countFriends)
    console.log(this.countComments)
    console.log(this.countPhotos)
    console.log(this.countGroups)
    console.log(this.fullActive)
    this.data_user.push(this.countPosts,
                        this.countFriends,
                        this.countComments,
                        this.countPhotos,
                        this.countGroups,
                        this.fullActive
                        )
    console.log(this.data_user)
  },
  computed: {
    countFriends: function() {
      return (this.person.friends_info).length
    },
    countPosts: function() {
      return (this.person.posts).length
    },
    countComments: function() {
      return ((this.person.comments).length + (this.person.comments_group).length)
    },
    countGroups: function() {
      return (this.person.all_groups).length
    },
    countPhotos: function() {
      return Math.floor(1 + Math.random()*4)
    },
    fullActive: function() {
      return ((this.person.comments).length + (this.person.comments_group).length + (this.person.posts).length)/2
    }
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
