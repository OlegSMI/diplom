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
          <SparklineChart :user_active="mass_data" class='absolute'/>
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
          <TheBestGraph :content="count_content" :users="mass_data" class='absolute'/>
        </v-sheet>
      </v-card-text>
    </v-card>
  </v-col>
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
      commentsUser: [],
      dates: new Object(),
      dates2: new Object(),
      mass_data: [],
      count_content: []
    }
  },
  beforeCreate(){
    this.$store.dispatch('loadItems')
    
  },
  created(){
    this.persons = this.$store.getters.getItems;
    for(var i in this.persons){
      this.posts.push({'name': this.persons[i].first_name +' '+ this.persons[i].last_name,
                       'posts': this.persons[i].posts,
                       })
      this.comments.push({'name': this.persons[i].first_name + this.persons[i].last_name, 
                          'comments': this.persons[i].comments,
                          'comments_group': this.persons[i].comments_group
                          })
    }
    console.log('jj',this.comments)
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
        this.commentsUser.push(this.comments[k].comments.length+this.comments[k].comments_group.length)
      }
      else if(this.comments[k].comments_group.length>0){
        this.commentsUser.push(this.comments[k].comments.length+this.comments[k].comments_group.length)
      }
      else{
        this.commentsUser.push(0)
      }
    }

    for (let i = 0; i < 24; i = i + 2){
      this.dates[i] = new Set();
      this.dates2[i] = [];
    }


    for (var z in this.posts){
      for (var h in this.posts[z].posts){
        for (let i = 0; i < 24; i = i + 2){
          var timepost = Number(this.posts[z].posts[h].timepost.split(':')[0])
          if (i <= timepost && timepost < i+2){
            this.dates[i].add(this.posts[z].name)
            this.dates2[i].push(1) 
          }   
        } 
      } 
    }


    for (var u in this.comments){
      for (var s in this.comments[u].comments){
        for (let i = 0; i < 24; i = i + 2){
          var timepost2 = Number(this.comments[u].comments[s].timecomment.split(':')[0])
          if (i <= timepost2 && timepost2 < i+2){
            this.dates[i].add(this.posts[z].name)
            this.dates2[i].push(1) 
          }   
        } 
      } 

      for (var g in this.comments[u].comments_group){
        for (let i = 0; i < 24; i = i + 2){
          var timepost3 = Number(this.comments[u].comments_group[g].timecomment.split(':')[0])
          if (i <= timepost3 && timepost3 < i+2){
            this.dates[i].add(this.posts[z].name)
            this.dates2[i].push(1) 
          }   
        } 
      } 
    }

    for (i in this.dates){
      if(this.dates[i].size===0){
        this.mass_data.push(0)
      }
      else{
        this.mass_data.push(this.dates[i].size)
      }
      
    }

    for (i in this.dates2){
      if(this.dates2[i].length===0){
        this.count_content.push(0)
      }
      else{
        this.count_content.push(this.dates2[i].length)
      }
      
    }


    console.log(this.mass_data)
    console.log(this.count_content)
  },
}
</script>