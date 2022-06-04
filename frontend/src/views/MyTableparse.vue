
<template>
  <div class="Dashboard">
    <h1 class="subheading grey--text pa-5">ВЫЯВЛЕННЫЕ ВОЕННОСЛУЖАЩИЕ:</h1>
    <v-container
    v-if="parseicon"
    class="text-md-center">
      <v-progress-circular
      :size="50"
      color="grey"
      indeterminate
    ></v-progress-circular>
    </v-container>
    <v-container
    v-else
    class="my-10" >
      
      <v-layout row class="mb-3">
        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn small text depressed class="grey--text ml-5" @click="sortBy('name')" v-on="on">
              <v-icon left small>mdi-account</v-icon>
              <span class="caption text-lowercase">Сортировать по имени</span>
            </v-btn>
          </template>
          <span>Убывание/Возрастание</span>
        </v-tooltip>

        <template >
          <v-btn small text depressed class="grey--text ml-5" @click="isPhoto('photo')" v-on="on" >
            <v-icon left small>mdi-account</v-icon>
            <span class="caption text-lowercase">Только с фото</span>
          </v-btn>
        </template>

      </v-layout>
        <v-expansion-panels flat>
          <v-expansion-panel
           v-for="task in tasks"
            :key="task.num_user"
            >
            <v-expansion-panel-header>
              <v-layout wrap :class="`pa-3 gig ${task.num_user}`">
                <v-col xs="2" md="2">
                  <div class="caption grey--text">Имя пользователя: </div>
                  <div>{{task.name}}</div>
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Был в сети: </div>
                  <div>{{task.online_status}}</div>
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Статус: </div>
                  <div>{{task.status}}</div>
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Фото: </div>
                  <v-img :src="task.photo" :alt="alt_name"></v-img>
                  <!-- <div>ФОТО</div> -->
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Город:</div>
                  <div>{{task.town}}</div>
                </v-col>
                <v-col xs="2" sm="4" md="2">
                  <div class="caption grey--text">Языки:</div>
                  <div>{{task.languages}}</div>
                </v-col>
              </v-layout>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-card flat>
                <v-card-text>
                  <v-layout>
                    <v-col>
                      <v-card
                      flat
                      class="pa-2"
                      color="#E9E9E9"
                      light
                      >
                        <v-card-title class="pa-2 grey--text">
                          <h5>Группы:</h5>
                        </v-card-title>
                        <div class="ma-2" v-for="group in task.groups" :key="group">
                          {{group.groups}}
                          <v-divider></v-divider>
                        </div>
                      </v-card>
                    </v-col>

                    <v-col>
                      <v-card
                      flat
                      class="pa-2"
                      color="#E9E9E9"
                      light
                      >
                        <v-card-title class="pa-2 grey--text">
                          <h5>Друзья:</h5>
                        </v-card-title>
                        <div class="ma-2" v-for="friend in task.friends" :key="friend">
                        {{friend.friends}}
                          <v-divider></v-divider>
                        </div>
                      </v-card>
                    </v-col>

            
                    
                    <v-col>
                      <v-card
                      flat
                      class="pa-2"
                      color="#E9E9E9"
                      light
                      >
                        <v-card-title class="pa-2 grey--text">
                          <h5>Посты:</h5>
                        </v-card-title>
                        <div class="ma-2" v-for="post in task.posts" :key="post">
                          {{post.posts}}
                          <v-divider></v-divider>
                        </div>
                      </v-card>
                    </v-col>

                    <v-col>
                      <v-card
                      flat
                      class="pa-2"
                      color="#E9E9E9"
                      light
                      >
                        <v-card-title class="pa-2 grey--text">
                          <h5>Комментарии:</h5>
                        </v-card-title>
                        <div class="ma-2" v-for="comment in task.comments" :key="comment">
                        {{comment.comments}}
                          <v-divider></v-divider>
                        </div>
                      </v-card>
                    </v-col>

                    <v-col>
                      <v-card
                      flat
                      class="pa-2"
                      color="#E9E9E9"
                      light
                      >
                        <v-card-title class="pa-2 grey--text">
                          <h5>Геолокации:</h5>
                        </v-card-title>
                        <div class="ma-2" v-for="locate in task.geolocation" :key="locate">
                        {{locate.location}}
                          <v-divider></v-divider>
                        </div>
                      </v-card>
                    </v-col>
                  </v-layout>
                </v-card-text>
                <router-link :to="{path:`/analizuser/$`, query: { id: task.num_user }}">
                  <v-btn text outlined>
                  <v-icon left>
                    mdi-chart-line
                  </v-icon>
                  Аналитика профиля
                  </v-btn>
                </router-link>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>        
        </v-expansion-panels>
        <div>
          <v-btn
          v-if="this.$store.getters.getState"
          text 
          outlined 
          class="ma-3 text-center"
          @click="exportExcel"
          >
            <v-icon left>
              mdi-apple-keyboard-caps
            </v-icon>
          Экспортировать
        </v-btn>
        </div>
        




    
    </v-container>
  </div>
  
</template>

<script>
import { saveExcel } from '@progress/kendo-vue-excel-export';
export default {
      data() {
          return {
              tasks: [],
              parseicon: false,
              count: 0,
              alt_name: ''
          }
      },
      created(){
        this.$store.dispatch('loadItems')
        
        if(this.$store.getters.getState===true){
          if(this.$store.getters.getCount===0){
            setTimeout(this.theOneFunc, 8 * 1000, 8);
            this.parseicon = true;
            this.tasks = this.$store.getters.getItems
            this.$store.dispatch('setCount', 1)
            console.log(this.$store.getters.getCount)
          }
          else{
            this.parseicon = false;
            this.tasks = this.$store.getters.getItems
          }
          
        }
      },
      methods: {
      sortBy(prop){
        if (this.count === 0){
          this.tasks.sort((a,b) => a[prop] < b[prop] ? -1 : 1);
          this.count = 1
        }
        else{
          this.tasks.sort((a,b) => a[prop] > b[prop] ? -1 : 1);
          this.count = 0
        }
      },
      theOneFunc(){
      this.parseicon = false
      },
      exportExcel () {
        console.log(this.tasks[0])
            saveExcel({
                data: this.tasks,
                fileName: "Users.xlsx",
                columns: [
                  { field: 'name', title: 'Имя'},
                  { field: 'user_id', title: 'Идентификатор'},
                  { field: 'online_status',  title: 'Был в сети'},
                  { field: 'photo',  title: 'Фото'},
                  { field: 'status',  title: 'Статус'},
                  { field: 'town',  title: 'Город'},
                  // { field: 'friends',  title: 'Друзья'},
              ]
            });
        },
      isPhoto (item){
        console.log(item)
        if(item === null){
          this.alt_name = 'Шляпа'
        }
      },
      analizUser(item){
        console.log(item)
      }
},
}
</script>
