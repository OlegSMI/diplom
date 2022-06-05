<template>
<v-container>

<v-card
    class="mx-auto text-center my-5"
    color="grey"
    dark
    max-width="900"
  >
  <v-card-text>
      <div class="text-h4 font-weight-thin">
        Общее число постов всех пользователей
      </div>
    </v-card-text>
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
        <BarPostsChart :posts="posts" class="absolute" />
      </v-sheet>
    </v-card-text>

    
  </v-card>

  <v-card
    class="mx-auto text-center my-5"
    color="grey"
    dark
    max-width="900"
  >
    <v-card-text>
      <div class="text-h4 font-weight-thin">
        Общее число комментариев всех пользователей
      </div>
    </v-card-text>
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
        <BarCommentsChart :comments="comments" class="absolute" />
      </v-sheet>
    </v-card-text>

  </v-card>

  <v-card
    class="mx-auto text-center my-5"
    color="grey"
    dark
    max-width="900"
  >
    <v-card-text>
      <div class="text-h4 font-weight-thin">
        Количество постов выявленных пользователей
      </div>
    </v-card-text>
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
        <RadarChart class='absolute'/>
      </v-sheet>
    </v-card-text>
  </v-card>

  <v-card
    class="mx-auto text-center my-5"
    color="grey"
    dark
    max-width="900"
  >
    <v-card-text>
      <div class="text-h4 font-weight-thin">
        Количество групп выявленных пользователей
      </div>
    </v-card-text>
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
        <DonutChart class='absolute'/>
      </v-sheet>
    </v-card-text>
  </v-card>

  <v-card
    class="mx-auto text-center my-5"
    color="grey"
    dark
    max-width="900"
  >
    <v-card-text>
      <div class="text-h4 font-weight-thin">
        Количество друзей выявленных пользователей
      </div>
    </v-card-text>
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
        <BarPostsChart class='absolute'/>
      </v-sheet>
    </v-card-text>
  </v-card>
</v-container>
  
  
</template>

<script>

import BarPostsChart from '../components/graphs/BarPostsComponent'
import BarCommentsChart from '../components/graphs/BarCommentsComponent'
// import SparklineChart from '../components/graphs/SparklinePostsComponent'
import RadarChart from '../components/graphs/RadialGraphPostComponent'
import DonutChart from '../components/graphs/DonutPostsComponent'
export default {
  components: { BarPostsChart, BarCommentsChart, RadarChart, DonutChart},
  data()  {
    return {
      persons: [],
      posts: [],
      comments: []
    }
  },
  beforeCreate(){
    this.$store.dispatch('loadItems')
    
  },
  created(){
    this.persons = this.$store.getters.getItems;
    console.log(this.persons)
    for(var i in this.persons){
      this.posts.push({'name': this.persons[i].name, 'posts': this.persons[i].posts})
      this.comments.push({'name': this.persons[i].name, 'comments': this.persons[i].comments})
    }
  },
}
</script>