
<template>
  <v-container fluid>
    <v-card>
      <v-sparkline
        :fill="fill"
        :gradient="selectedGradient"
        :line-width="width"
        :padding="padding"
        :smooth="radius || false"
        :value="value"
        auto-draw
      ></v-sparkline>

      <v-divider></v-divider>

      <v-row>
        <v-col
          cols="12"
          md="6"
        >
          <v-row
            class="fill-height"
            align="center"
          >
            <v-item-group
              v-model="selectedGradient"
              mandatory
            >
            </v-item-group>
          </v-row>
        </v-col>
      </v-row>
    </v-card>  
    <v-card>
      <bar-graph
      title="Test Bar Graph"
      animDuration="1s"
      :showValues="true"
      :easeIn="true"
      :points="points"
      :labels="labels"
      :width="1024"
      :height="320"
    />
    </v-card>
  </v-container>

</template>

<script>
  export default {
    data() {
      return {
      points: [42, 8, 15, 16, 23, 42, 4, 8, 15],
      labels: [
        "Label 1",
        "Label 2",
        "Label 3",
        "Label 4",
        "Label 5",
        "Label 6",
        "Label 7",
        "Label 8",
        "Label 9"
      ]
      };
    }
  };
</script>

<script>
import axios from 'axios'
  const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
  ]

  export default {
    data: () => ({
      fill: false,
      selectedGradient: gradients[3],
      gradients,
      padding: 10,
      radius: 10,
      value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
      width: 2,
      tasks: ['']
    }),
    methods: {
      async getData() {
              try {
                  const response = await axios.get('http://localhost:8000/users');
                  this.tasks = response.data;
              } catch (error) {
                  console.log(error);
              }
          },
      },
      created() {
            this.getData();
      }
  }
</script>