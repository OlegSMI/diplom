<template>
<v-container>

<v-card
    class="mx-auto text-center my-5"
    color="#A3AF9C"
    dark
    max-width="900"
  >
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)" elevation="4" rounded>
        <!-- <BarChart /> -->
      </v-sheet>
    </v-card-text>

    <v-card-text>
      <div class="text-h4 font-weight-thin">
        Число представляющих интерес постов
      </div>
    </v-card-text>
  </v-card>

  <v-card
    class="mx-auto text-center my-5"
    color="#A3AF9C"
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
        <v-sparkline
          class="py-6"
          :value="value"
          :labels="users"
          color="rgba(255, 255, 255, .7)"
          height="100"
          padding="24"
          stroke-linecap="round"
          smooth
          type="bar"
          line-width="10"
        >
          <template v-slot:label="item">
            User: {{ item.value }}
          </template>
          <template v-slot:key="item">
            User: {{ item.value }}
          </template>
        </v-sparkline>
      </v-sheet>
    </v-card-text>

  </v-card>

  <v-card
    class="mx-auto text-center my-5"
    color="#A3AF9C"
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
        <v-sparkline
          class="py-6"
          :value="value"
          :labels="users"
          color="rgba(255, 255, 255, .7)"
          height="100"
          padding="24"
          stroke-linecap="round"
          smooth
        >
          <template v-slot:label="item">
            ${{ item.value }}
          </template>
        </v-sparkline>
        
      </v-sheet>
    </v-card-text>
  </v-card>

  <v-card
    class="mx-auto text-center my-5"
    color="#A3AF9C"
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
        <v-sparkline
          class="py-6"
          :value="value"
          :labels="users"
          color="rgba(255, 255, 255, .7)"
          height="100"
          padding="24"
          stroke-linecap="round"
          smooth
        >
          <template v-slot:label="item">
            ${{ item.value }}
          </template>
        </v-sparkline>
      </v-sheet>
    </v-card-text>
  </v-card>

  <v-card
    class="mx-auto text-center my-5"
    color="#A3AF9C"
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
        <v-sparkline
          class="py-6"
          :value="value"
          :labels="users"
          color="rgba(255, 255, 255, .7)"
          height="100"
          padding="24"
          stroke-linecap="round"
          smooth
          
        >
          <template v-slot:label="item">
            ${{ item.value }}
          </template>
        </v-sparkline>
      </v-sheet>
    </v-card-text>
  </v-card>
</v-container>
  
  
</template>

<script>

// import BarChart from '../components/graphs/BarPostsComponent'
export default {
  // components: { BarChart },
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