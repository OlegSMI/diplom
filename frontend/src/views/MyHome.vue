<template>
  <div class="Dick">
    <h1 class="subheading grey--text pa-5">Выявление военнослужащих иностранных государств</h1>

    <v-container class="my-5">
      <v-layout row wrap>
         <v-col xs="12" sm="6" md="4" lg="3" v-for="person in team" :key=person.name>
           <v-card flat class="text-center ma-3">
             <v-responsive class="pt-4">
              <v-avatar size="100" class="grey lighten-2">
                <v-img :src="getImgUrl(person.avatar)" alt="sisichka"></v-img>
              </v-avatar>
             </v-responsive>
            <v-card-text>
              <div class="subheading">{{person.name}}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="grey" @click="get_parse">
                <v-icon left>mdi-arrow-right-bold-hexagon-outline</v-icon>
                <span>Запустить</span>
              </v-btn>
            </v-card-actions>
            <v-card-actions>
              <v-btn text color="grey" @click="stop_parse">
                <v-icon left>mdi-close-octagon</v-icon>
                <span>Остановить</span>
              </v-btn>
            </v-card-actions>
            <!-- <v-text-field
              v-if="this.load==true"
              value="Идет парсинг"
              label="Solo"
              color="green"
              solo
              disabled
            ></v-text-field> -->
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
      load: false,
      team: [
        { name: 'Парсер "ВКонтакте"', avatar:  'vk.png' },
        { name: 'Парсер "Фэйсбук"', avatar: 'Facebook.png' },
        { name: 'Парсер "Страва"', avatar: 'strava.svg' },
        { name: 'Парсер "ТестНет"', avatar: 'wifi.jpg' },
      ]
    }
  },
    methods: {
    getImgUrl(pic){
      return require('../assets/' + pic)
    },
    get_parse(){
      this.load = true;
    },
    stop_parse(){
      this.load = false;
    }
  }

}
</script>