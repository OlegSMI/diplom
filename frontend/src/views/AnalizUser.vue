<template>
  <div class="about">
    <v-row>
      <v-col md="4">
        <v-card 
        class="mx-auto text-center my-5"
        color="grey"
        dark
        max-width="900"
        >
          <v-card-text>
            <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
              <RadarChart class='absolute'/>
            </v-sheet>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col md="8" >
        <v-card
        class="mx-auto text-center my-5"
        color="grey"
        dark
        max-width="900"
        >
          <v-card-text>
            <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
              <SparklineChart class='absolute'/>
            </v-sheet>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>


<script>
import SparklineChart from '../components/graphs/SparklinePostsComponent'
import RadarChart from '../components/graphs/RadialGraphPostComponent'
export default {
  components: { SparklineChart, RadarChart },
  
}
</script>
