<template>
  <div class="menu" style="margin: 10px">
    <h1>Dishes</h1>
    <v-data-table
      :headers="headers"
      :items="dishes"
      :items-per-page="5"
      class="elevation-1"
      @update:options="onOptionUpdated"
    ></v-data-table>
    <AddDish style="padding-top: 18px" />
    <!-- <router-link class="btn btn-light btn-outline-primary" to="/restaurant/add"
        >Add Restaurant</router-link
      > -->
  </div>
</template>

<script>
import { getDishes } from "@/rest";
import AddDish from "./AddDish.vue";

export default {
  name: "DishName",
  components: {
    AddDish,
  },
  data() {
    return {
      headers: [
        {
          text: "Dish name",
          sortable: true,
          value: "DishName",
        },
        {
          text: "Restaurant Name",
          sortable: true,
          value: "Restaurant",
        },
        {
          text: "Taste",
          sortable: false,
          value: "Taste",
        },
        {
          text: "Price",
          sortable: true,
          value: "Price",
        },
        {
          text: "Rating",
          sortable: true,
          value: "Rating",
        },
      ],
      name: "",
      dishes: [],
    };
  },
  props: {},
  async mounted() {
    let result = await getDishes();
    console.warn(result);
    this.dishes = result.data;
  },
  methods: {
    onOptionUpdated(option) {
      console.log(option);
    },
  },
};
</script>
