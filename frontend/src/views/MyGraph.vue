<template>
<v-container>
<v-row>
   <v-col md="6">
    <v-card
    class="text-center"
    color="white"
    dark
    flat
    max-width="900"
    >
      <v-card-text>
        <div class="text-h5 black--text">
          Общее число постов выявленных пользователей
        </div>
      </v-card-text>
      <v-card-text>
        <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
          <BarPostsChart :users="users" :postsUser="postsUser" class="absolute" />
        </v-sheet>
      </v-card-text>
    </v-card>
   </v-col>
   <v-col md="6">
     <v-card
    class="text-center"
    color="white"
    dark
    flat
    max-width="900"
    >
      <v-card-text>
        <div class="text-h5 black--text">
          Общее число комментариев выявленных пользователей
        </div>
      </v-card-text>
      <v-card-text>
        <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
          <BarCommentsChart :users="users" :commentsUser="commentsUser" class="absolute" />
        </v-sheet>
      </v-card-text>
    </v-card>
   </v-col>
</v-row>
<v-row>
  <v-col md="6">
    <v-card
    class="text-center"
    color="white"
    dark
    flat
    max-width="900"
    >
      <v-card-text>
        <div class="text-h5 black--text">
          Наибольшая активность пользователей
        </div>
      </v-card-text>
      <v-card-text>
        <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
          <SparklineChart class='absolute'/>
        </v-sheet>
      </v-card-text>
    </v-card>
  </v-col>
  <v-col md="6">
    <v-card
    class="text-center"
    color="white"
    dark
    flat
    max-width="900"
    >
      <v-card-text>
        <div class="text-h5 black--text">
          Группы и посты с военной тематикой 
        </div>
      </v-card-text>
      <v-card-text>
        <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
          <DonutChart class='absolute'/>
        </v-sheet>
      </v-card-text>
    </v-card>
  </v-col>
</v-row>
<v-row>
  <v-col md="12">
    <v-card
    class="text-center"
    color="white"
    dark
    flat
    >
      <v-card-text>
        <div class="text-h5 black--text">
          Наибольшая активность выявленных пользователей по месяцам
        </div>
      </v-card-text>
      <v-card-text>
        <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
          <TheBestGraph class='absolute'/>
        </v-sheet>
      </v-card-text>
    </v-card>
  </v-col>
</v-row>
<v-row>
      <v-card>
        <TheBestGraph class='absolute'/>
      </v-card>
    </v-row>
  

  

  

  

  
</v-container>
  
  
</template>

<script>

import BarPostsChart from '../components/graphs/BarPostsComponent'
import BarCommentsChart from '../components/graphs/BarCommentsComponent'
import SparklineChart from '../components/graphs/SparklinePostsComponent'
// import RadarChart from '../components/graphs/RadialGraphPostComponent'
import DonutChart from '../components/graphs/DonutPostsComponent'
import TheBestGraph from '@/components/graphs/TheBestGraph.vue'
export default {
  components: { BarPostsChart, BarCommentsChart, DonutChart, SparklineChart, TheBestGraph },
  data()  {
    return {
      persons: [],
      posts: [],
      comments: [],
      users: [],
      postsUser: [],
      commentsUser: []
    }
  },
  beforeCreate(){
    this.$store.dispatch('loadItems')
    
  },
  created(){
    this.persons = this.$store.getters.getItems;
    for(var i in this.persons){
      this.posts.push({'name': this.persons[i].name, 'posts': this.persons[i].posts})
      this.comments.push({'name': this.persons[i].name, 'comments': this.persons[i].comments})
    }
    for (var j in this.posts){
      this.users.push(this.posts[j].name)
      if(this.posts[j].posts.length>0){
        this.postsUser.push(this.posts[j].posts.length) 
      }
      else{
        this.postsUser.push(0)
      }
    }
    for (var k in this.comments){
      if(this.comments[k].comments.length>0){
        this.commentsUser.push(this.comments[k].comments.length)
      }
      else{
        this.commentsUser.push(0)
      }
    }
  },
}
</script>