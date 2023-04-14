<template>
  <div class="restaurant" style="margin: 10px">
    <h1>Restaurant</h1>
    <v-data-table
      :headers="headers"
      :items="restaurants"
      :items-per-page="5"
      class="elevation-1"
      @update:options="onOptionUpdated"
    ></v-data-table>
    <AddRestaurant style="padding-top: 18px" />
    <!-- <router-link class="btn btn-light btn-outline-primary" to="/restaurant/add"
      >Add Restaurant</router-link
    > -->
  </div>
</template>

<script>
import { getRestaurants } from "@/rest";
import AddRestaurant from "./AddRestaurant.vue";

export default {
  name: "RestaurantName",
  components: {
    AddRestaurant,
  },
  data() {
    return {
      headers: [
        {
          text: "Restaurant Id",
          sortable: true,
          value: "RestaurantId",
        },
        {
          text: "Restaurant Name",
          sortable: true,
          value: "RestaurantName",
        },
        {
          text: "Restaurant Intro",
          sortable: false,
          value: "RestaurantIntro",
        },
      ],
      name: "",
      restaurants: [],
    };
  },
  props: {},
  async mounted() {
    let result = await getRestaurants();
    console.warn(result);
    this.restaurants = result.data;
  },
  methods: {
    onOptionUpdated(option) {
      console.log(option);
    },
  },
};
</script>
