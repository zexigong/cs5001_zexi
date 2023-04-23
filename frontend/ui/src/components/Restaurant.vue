<template>
  <div class="restaurant" style="margin: 10px">
    <h1>Restaurant</h1>
    <v-text-field
      v-model="search"
      append-icon="mdi-magnify"
      label="Search"
      single-line
      hide-details
      clearable
      @click:append="onSearch"
    ></v-text-field>
    <v-data-table
      :headers="headers"
      :items="restaurants"
      :items-per-page="5"
      class="elevation-1"
      @update:options="fetchData"
      :search="search"
      :options.sync="options"
      :server-items-length="itemsNum"
      :loading="loading"
      aria-disabled="true"
    >
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small class="mr-2" @click="deleteItem(item)"> mdi-delete </v-icon>
      </template></v-data-table
    >
    <AddRestaurant style="padding-top: 18px" @fetch-data="fetchData" />
    <EditRestaurant
      :restaurantToEdit="restaurantToEdit"
      :trigger-edit="triggerEdit"
      @fetch-data="fetchData"
    />
    <!-- <router-link class="btn btn-light btn-outline-primary" to="/restaurant/add"
      >Add Restaurant</router-link
    > -->
  </div>
</template>

<script>
import { getRestaurants, deleteRestaurant } from "@/rest";
import AddRestaurant from "./AddRestaurant.vue";
import EditRestaurant from "./EditRestaurant.vue";

export default {
  name: "RestaurantName",
  components: {
    AddRestaurant,
    EditRestaurant,
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
        { text: "Actions", value: "actions", sortable: false },
      ],
      name: "",
      restaurants: [],
      search: "",
      itemsNum: 0,
      options: {},
      loading: false,
      editEnabled: false,
      triggerEdit: false,
      restaurantToEdit: {},
    };
  },
  props: {},
  methods: {
    async fetchData(options = this.options) {
      this.loading = true;
      let params = {
        page: options.page,
        itemsPerPage: options.itemsPerPage,
        sortBy: options.sortBy ? options.sortBy[0] : null,
        sortDesc: options.sortDec ? options.sortDec[0] : null,
        search: this.search !== "" ? this.search : null,
      };
      let result = await getRestaurants(params);
      this.loading = false;
      console.log(options);
      console.warn(result);
      this.restaurants = result.data.data;
      this.itemsNum = result.data.itemsNum;
    },
    async onSearch() {
      this.fetchData(this.options);
    },
    editItem(restaurant) {
      this.restaurantToEdit = restaurant;
      this.triggerEdit = !this.triggerEdit;
    },
    async deleteItem(restaurant) {
      await deleteRestaurant(restaurant.RestaurantId);
      this.fetchData();
    },
  },
};
</script>
