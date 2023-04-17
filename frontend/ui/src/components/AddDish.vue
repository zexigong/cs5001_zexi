<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="888">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on"> Add Dish </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2"> Add Dish </v-card-title>
        <v-card-text>
          <v-form v-model="valid">
            <v-container>
              <v-row>
                <v-col cols="12" md="4">
                  <v-text-field
                    v-model="dishName"
                    :rules="nameRules"
                    :counter="88"
                    label="Dish name"
                    required
                  ></v-text-field>
                </v-col>

                <v-col cols="30" md="4">
                  <v-text-field
                    v-model="restaurantName"
                    :counter="88"
                    label="Restaurant Name"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-text-field
                    v-model="Taste"
                    :rules="nameRules"
                    :counter="88"
                    label="Taste"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-text-field
                    v-model="Price"
                    :rules="nameRules"
                    :counter="88"
                    label="Price"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-text-field
                    v-model="Rating"
                    :rules="nameRules"
                    :counter="88"
                    label="Rating"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="second" text @click="dialog = false"> Cancel </v-btn>
          <v-btn color="primary" text @click="onAdd"> Add </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialog2" width="388">
      <v-card-text class="text-h5 grey lighten-2">
        {{ this.text }}
      </v-card-text>
    </v-dialog>
  </div>
</template>
<script>
import { addDishes } from "@/rest";
export default {
  name: "AddDishes",

  data() {
    return {
      valid: false,
      dialog: false,
      dialog2: false,
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => v.length <= 88 || "Name must be less than 88 characters",
      ],
      dishName: "",
      restaurantName: "",
      Taste: "",
      Price: "",
      Rating: "",
      text: "",
    };
  },
  methods: {
    async onAdd() {
      const result = await addDishes({
        DishName: this.dishName,
        Restaurant: this.restaurantName,
        Taste: this.Taste,
        Price: this.Price,
        Rating: this.Rating,
      });
      console.log(result);
      this.text = result.data;
      this.dialog = false;
      this.dialog2 = true;
    },
  },
};
</script>
