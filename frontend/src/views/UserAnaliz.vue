<template>
  <v-card
    class="mx-auto text-center my-5"
    color="#A3AF9C"
    dark
    max-width="900"
  >
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)">
        <v-sparkline
          :value="value"
          :labels="calue"
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

    <v-card-text>
      <div class="text-h4 font-weight-thin">
        Частота постов пользователя
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
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
      calue: [
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