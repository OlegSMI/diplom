<template >
  <v-app>
    <Navbar />
    <v-content mx-4 class="grey lighten-4" id="app">
      <router-view :vision="vision"  @updateVision="vision = $event"/>
    </v-content>
  </v-app>
  
</template>


<script>
import Navbar from './components/MyNavbar'

export default {
  name: 'App',
  components: { Navbar },
  data () {
    return {
      vision: false
    }
  }
}
</script>
