<template>
  <div>
    <h1 class="subheading grey--text pa-5">Выявление военнослужащих иностранных государств</h1>

    <v-container class="my-5">
      <v-layout row wrap>
        {{items}}
         <v-col xs="12" sm="6" md="4" lg="3" v-for="person in team" :key=person.name>
           <v-card flat class="text-center ma-3">
             <v-responsive class="pt-4">
              <v-avatar size="100" class="grey lighten-2">
                <v-img :src="getImgUrl(person.avatar)"></v-img>
              </v-avatar>
             </v-responsive>
            <v-card-text>
              <div class="subheading">{{person.name}}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="grey" @click="get_parse(person)" >
                <v-icon left>mdi-arrow-right-bold-hexagon-outline</v-icon>
                <span>Запустить</span>
              </v-btn>
            </v-card-actions>
            <v-card-actions>
              <v-btn text color="grey" @click="stop_parse(person)">
                <v-icon left>mdi-close-octagon</v-icon>
                <span>Остановить</span>
              </v-btn>
            </v-card-actions>
           </v-card>
          <v-card
          flat
          class="text-center ma-3"
          >
            <v-switch
              v-model="switch_check1"
              v-if="person.switches==switch_check1"
              class="pa-3"
              disabled
              label="Парсер не работает"
              hide-details
            ></v-switch>
            
            <v-switch
              v-model="switch_check2"
              v-else
              class="pa-3"
              disabled
              label="Парсер работает"
              hide-details
            ></v-switch>
          </v-card>
           
            
         </v-col>  
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {

  data() {
    return {
      tasks: [''],
      switch_check1: '',
      switch_check2: '',
      team: [
        { id: 1, name: 'Парсер "ВКонтакте"', avatar:  'vk.png',  switches: false},
        { id: 2, name: 'Парсер "Фэйсбук"', avatar: 'Facebook.png', switches: false},
        { id: 3,  name: 'Парсер "Страва"', avatar: 'strava.svg', switches: false},
        { id: 4,  name: 'Парсер "ТестНет"', avatar: 'wifi.jpg', switches: this.$store.getters.getState},
      ]
    }
  },

  created(){
    this.switch_check1 = this.$store.getters.getState
    this.switch_check2 = !this.$store.getters.getState
  },
  
  methods: {
  getImgUrl(pic){
    return require('../assets/' + pic)
  },
  get_parse(item){
    item.switches = true;
    if (item.id === 4){
      this.$store.dispatch('setState', true)
    }
  },
  stop_parse(item){
    item.switches = false;
    if (item.id === 4){
      this.$store.dispatch('setState', false)
    }
  }
  },
}
</script>



