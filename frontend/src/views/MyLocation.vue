<template>
<v-card flat style="background: transparent"> 
    <v-row>
        <v-col md="4">
            <v-card class="ma-5" flat>
                <v-card-title>
                    Данные:
                </v-card-title>
                <v-card-text>
                  <v-text-field
                      label="Левая широта"
                      hide-details="auto"
                      class="ma-2"
                      :value="latitude_1"
                      >
                      </v-text-field>
                  <v-text-field
                      label="Левая долгота"
                      hide-details="auto"
                      class="ma-2"
                      :value="longitude_1"
                      ></v-text-field>
                  <v-text-field
                      label="Правая широта"
                      hide-details="auto"
                      class="ma-2"
                      :value="latitude_2"
                      ></v-text-field>
                  <v-text-field
                      label="Правая долгота"
                      hide-details="auto"
                      class="ma-2"
                      :value="longitude_2"
                      ></v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-btn
                    :color="$route.meta.theme"
                    class="ma-2 black--text"
                    @click="get_coordinates"
                    text
                    outlined
                    >
                    Загрузить
                    <v-icon right>
                    mdi-animation-outline
                    </v-icon>
                    </v-btn>
                    
                </v-card-actions>
                <v-progress-linear
                        v-if="this.load==true"
                        indeterminate
                        color="primary"
                ></v-progress-linear>
              <v-card-text>
                <v-data-table
                :headers="headers"
                :items="users_info"
                item-key="name"
                class="elevation-1"
                :search="search"
                v-if="users_info.length>0"
              >
                <template v-slot:top>
                  <v-text-field
                    v-model="search"
                    label="Поиск (ЗАГЛАВНЫМИ БУКВАМИ)"
                    class="mx-4"
                  ></v-text-field>
                </template>
                <template v-slot:[`item.actions`]="{ item }">
                  <v-icon
                    small
                    class="mr-2"
                    @click="getroute(item)"
                  >
                    mdi-pencil
                  </v-icon>
                </template>
              </v-data-table>
                <v-btn 
                    v-if="users_info.length>0"
                    :color="$route.meta.theme"
                    class="mt-5 black--text"
                    @click="exportExcel"
                    text
                    outlined
                  >
                    Экспортировать
                  <v-icon right>
                    mdi-apple-keyboard-caps
                  </v-icon>
                </v-btn>
              </v-card-text> 
            </v-card>
        </v-col>
      <v-col md="8">
        <v-card flat style="background: transparent" class="my-5 mr-5">
          <Map :coords="coords" :first_coord="first_coord"
           :user="user" :center="center" :zoom="zoom" style='height: 650px; width: 100%'/>
        </v-card>
      </v-col>
    </v-row>
</v-card>
</template>






<script>
 /* eslint-disable */
import axios from 'axios'
import Map from "@/components/map/MapStrava.vue";
import { saveExcel } from '@progress/kendo-vue-excel-export';

export default {
    name: 'location',
    props: {
      latitude_1: {
      default: () => { return 59.937 }
    },
      longitude_1:  {
      default: () => { return 30.3089 }
      },
      latitude_2: {
      default: () => { return 52.673 }
    },
      longitude_2:  {
      default: () => { return 29.345 }
      },
    },
    components: {
    Map,
  },

  data: () => ({
    coords: [],
    user:'',
    users_info: [],
    center: [59.937, 30.3089],
    first_coord: [],
    load: false,
    zoom: 10,
    // Таблица
    search: '',
    headers: [
          {
            text: 'Ф.И.О.',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Маршрут', value: 'actions', sortable: false },
        ],
  }),

  watch: {
    title(val) {
      this.lot = val;
    },
  },
methods: {
    async get_coordinates() {
      this.load = true;
      const response = await axios.get('http://127.0.0.1:8000/geo/polyline/');
      this.users_info = response.data;
      this.load = false;
      console.log('you click');
  },
    getroute(route){
      this.coords = route.coordinates
      this.user = route.name
      this.center = this.coords[0]
      this.zoom = 15
  },
    exportExcel () {

            saveExcel({
                data: this.users_info,
                fileName: "Routes.xlsx",
                columns: [
                  { field: 'name', title: 'Имя'},
                  { field: 'id', title: 'Идентификатор'},
                  { field: 'coordinates',  title: 'Маршрут'},
              ]
            });
        },
  },
created() {
  this.center = [this.latitude_1, this.longitude_1]
  this.first_coord = [this.latitude_1+0.005, this.longitude_1+0.005]
  console.log(this.first_coord)
},
  computed: {
    url() {
      if (!this.points[0]['2']['codingline']) return;
      return URL.createObjectURL(this.points[0]['2']['codingline']);
    }
  },
};
</script>
