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
        Число представляющих интерес постов
      </div>
    </v-card-text>
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
        <BarChart class="absolute" />
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
        Число представляющих интерес постов
      </div>
    </v-card-text>
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
        <SparklineChart class='absolute'/>
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
        <SparklineChart class='absolute'/>
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
        <BarChart class='absolute'/>
      </v-sheet>
    </v-card-text>
  </v-card>
</v-container>
  
  
</template>

<script>

import BarChart from '../components/graphs/BarPostsComponent'
import SparklineChart from '../components/graphs/SparklinePostsComponent'
import RadarChart from '../components/graphs/RadialGraphPostComponent'
export default {
  components: { BarChart, SparklineChart, RadarChart, },
  data: () => ({
    value: [
      423,
      446,
      675,
      510,
      590,
      610,
      760,
    ],
    users: [
      1,
      3,
      6,
      9,
      12,
      2,
      1111,
    ],
  }),
}
</script>