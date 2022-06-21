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
        height="485"
        flat
        max-width="900"
        >
          <v-card-text>
            <h2 class="black--text font-weight-thin ma-2">
              Действия пользователя:
            </h2>
              <!-- <HeatChart :person="person" class='absolute'/> -->
              <v-list v-for="el in person.posts" :key="el">
                <v-list-item style="background-color: lightgrey; border-radius:20px;">
                  {{el.post_text}}
                </v-list-item>
              </v-list>
              <v-list v-for="el in person.comments" :key="el">
                <v-list-item style="background-color: lightgrey; border-radius:20px;">
                  {{el.comment_text}}
                </v-list-item>
              </v-list>
              <v-list v-for="el in person.comments_group" :key="el">
                <v-list-item style="background-color: lightgrey; border-radius:20px;">
                  {{el.comment_text}}
                </v-list-item>
              </v-list>
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
                Наибольшая активность
              </h2>
              <BestChart :dates="count_content" class='absolute'/>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>


<script>
import RadarChart from '../components/graphs/RadialGraphPostComponent'
// import HeatChart from '../components/graphs/HeatMapComponent'
import BestChart from '../components/graphs/TheBestGraphUser'
export default {
  components: {RadarChart, BestChart},
  data() {
    return {
      person: [],
      times: [],
      data_user:[],
      dates: [],
      count_content: []
    }
  },
  created(){
    this.person = this.$store.getters.getTodoById(Number(this.$route.query.num))
    console.log(this.person.posts)

    for (let i = 0; i < 24; i = i + 2){
      this.dates[i] = [];
    }

    for (var h in this.person.posts){
        for (let i = 0; i < 24; i = i + 2){
          var timepost = Number(this.person.posts[h].timepost.split(':')[0])
          if (i <= timepost && timepost < i+2){
            this.dates[i].push(1) 
          }   
        } 
    }

    for (var u in this.person.comments){
        for (let i = 0; i < 24; i = i + 2){
          var timepost2 = Number(this.person.comments[u].timecomment.split(':')[0])
          if (i <= timepost2 && timepost2 < i+2){
            this.dates[i].push(1) 
          }   
      }  
    }
    for (var g in this.person.comments_group){
      for (let i = 0; i < 24; i = i + 2){
        var timepost3 = Number(this.person.comments_group[g].timecomment.split(':')[0])
        if (i <= timepost3 && timepost3 < i+2){
          this.dates[i].push(1) 
        }   
      } 
    }
    for (var i in this.dates){
      if(this.dates[i].length===0){
        this.count_content.push(0)
      }
      else{
        this.count_content.push(this.dates[i].length)
      }
      
    }


    this.data_user.push(this.countPosts,
                        this.countFriends,
                        this.countComments,
                        this.countPhotos,
                        this.countGroups,
                        this.fullActive
                        )
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
      // return Math.floor(1 + Math.random()*4)
      return 1
    },
    fullActive: function() {
      return ((this.person.comments).length + (this.person.comments_group).length + (this.person.posts).length)/2
    }
  }
}
</script>
