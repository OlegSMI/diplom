<template>
  <div class="about">
    <v-card flat class="ma-5 pa-5" >
      <h1>Чуханина:</h1>
      {{infouser}}
    </v-card>
    
  </div>
</template>


<script>
export default {
   data() {
          return {
              infouser: [],
          }
      },
  created(){
    this.infouser = this.$route.params.task
  }
}
</script>
