<template> 
  <nav>
    <v-app-bar text app color="spacegray">

      <v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-light">МЕНЮ</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn depressed class="text-uppercase grey--text"> 
        <v-icon class="text-uppercase grey--text">mdi-logout-variant</v-icon>
        Выйти
      </v-btn>

    </v-app-bar>

    <v-navigation-drawer app v-model="drawer" class="grey">
      <v-row justify="center">
        <v-col>
          <Popup />
        </v-col>
      </v-row>
      <v-list>
        <v-list-tile v-for="link in links" :key="link.text" > 
          <v-list-item :to="link.route">
            <v-icon class="white--text">{{link.icon}}</v-icon>
            <v-list-tile-title class="white--text ml-5">{{link.text}}</v-list-tile-title>
          </v-list-item>
          <v-list-tile-content>
         
          </v-list-tile-content>

        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
  </nav>
     
</template>

<script>
import Popup from './MyPopup'
  export default {
    components: {
      Popup
    },
    data: () => {
      return {
        drawer:false,
        links: [
          { icon: 'mdi-account-search', text: 'Парсинг', route: '/'},
          { icon: 'mdi-chart-line', text: 'График по выявленным', route: '/projects'},
          { icon: 'mdi-account-arrow-up', text: 'Список выявленных', route: '/tableparse'},
          { icon: 'mdi-book-open-outline', text: 'Описание', route: '/about'},
          { icon: 'mdi-map-outline', text: 'Геолокация', route: '/location'},
          { icon: 'mdi-chart-box-outline', text: 'Диаграмма', route: '/diagrams'},
        ]

      }
    } 
  }
</script>
