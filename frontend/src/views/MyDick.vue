
<template>
  <div class="Dashboard">
    <h1 class="subheading grey--text pa-5">ВЫЯВЛЕННЫЕ ВОЕННОСЛУЖАЩИЕ:</h1>

    <v-container class="my-10">
      <v-layout row class="mb-3">
        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn small text depressed class="grey--text ml-5" @click="sortBy('name')" v-on="on">
              <v-icon left small>mdi-account</v-icon>
              <span class="caption text-lowercase">Фильтр по имени</span>
            </v-btn>
          </template>
          <span>Убывание/Возрастание</span>
        </v-tooltip>

        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn small text depressed class="grey--text ml-5" @click="sortBy('groups')" v-on="on" >
              <v-icon left small>mdi-account</v-icon>
              <span class="caption text-lowercase">Фильтр по очку</span>
            </v-btn>
          </template>
          <span>dick</span>
        </v-tooltip>
      </v-layout>



        <v-expansion-panels>
          <v-expansion-panel v-for="task in tasks" :key="task.infouser.num_user">
            <v-expansion-panel-header>
              <v-layout wrap :class="`pa-3 gig ${task.infouser}`">
                <v-col xs="2" md="2">
                  <div class="caption grey--text">Имя пользователя: </div>
                  <div>{{task.infouser.name}}</div>
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Был в сети: </div>
                  <div>{{task.infouser.online_status}}</div>
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Статус: </div>
                  <div>{{task.infouser.status}}</div>
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Фото: </div>
                  <div>ФОТО</div>
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Город:</div>
                  <div>{{task.infouser.town}}</div>
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Языки:</div>
                  <div>{{task.infouser.languages}}</div>
                </v-col>
              </v-layout>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-card flat>
                <v-card-text>
                  <v-layout>
                    <v-col>
                      <div class="caption grey--text">Группы:</div>
                      <div v-for="group in task.groups" :key="group">·{{group.groups}}</div>
                    </v-col>
                    <v-col>
                      <div class="caption grey--text">Друзья:</div>
                      <div v-for="friend in task.friends" :key="friend">·{{friend.friends}}</div>
                    </v-col>
                    <v-col>
                      <div class="caption grey--text">Друзья:</div>
                      <div v-for="friend in task.friends" :key="friend">·{{friend.friends}}</div>
                    </v-col>
                    <v-col>
                      <div class="caption grey--text">Посты:</div>
                      <div v-for="post in task.posts" :key="post">·{{post.posts}}</div>
                    </v-col>
                    <v-col>
                      <div class="caption grey--text">Комментарии:</div>
                      <div v-for="comment in task.comments" :key="comment">·{{comment.comments}}</div>
                    </v-col>
                    <v-col>
                      <div class="caption grey--text">Геолокации:</div>
                      <div v-for="locate in task.geolocation" :key="locate">·{{locate.location}}</div>
                    </v-col>
                  </v-layout>
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>        
        </v-expansion-panels>



        <v-divider></v-divider>
    
    </v-container>
  </div>
  
</template>

<style>

.gig.hulia {
  border-left: 4px solid #3cd1c2;
}

.gig.honor {
  border-left: 4px solid green;
}

.gig.salamalekum {
  border-left: 4px solid tomato;
}

.v-chip.hulia {
   background: #3cd1c2 !important;
}

.v-chip.honor {
  background: green !important;
}

.v-chip.salamalekum {
  background: tomato !important;
}

</style>

<script>
import axios from 'axios'
export default {
      data() {
          return {
              tasks: [''],
          }
      },
      methods: {
          async getData() {
              try {
                  const response = await axios.get('http://localhost:8000/users');
                  this.tasks = response.data;
              } catch (error) {
                  console.log(error);
              }
          },
          sortBy(prop){
      this.infouser.sort((a,b) => a[prop] < b[prop] ? -1 : 1);
    }
      },
      created() {
            this.getData();
      }
}
</script>
