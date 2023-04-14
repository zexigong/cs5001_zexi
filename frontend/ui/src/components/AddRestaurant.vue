<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="888">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on"> Add Restaurant </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2"> Add Restaurant </v-card-title>
        <v-card-text>
          <v-form v-model="valid">
            <v-container>
              <v-row>
                <v-col cols="12" md="4">
                  <v-text-field
                    v-model="restaurantName"
                    :rules="nameRules"
                    :counter="88"
                    label="Restaurant name"
                    required
                  ></v-text-field>
                </v-col>

                <v-col cols="30" md="4">
                  <v-text-field
                    v-model="restaurantIntro"
                    :counter="388"
                    label="Restaurant intro"
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
import { addRestaurant } from "@/rest";
export default {
  name: "AddRestaurant",

  data() {
    return {
      valid: false,
      dialog: false,
      dialog2: false,
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => v.length <= 88 || "Name must be less than 88 characters",
      ],
      restaurantName: "",
      restaurantIntro: "",
      text: "",
    };
  },
  methods: {
    async onAdd() {
      const result = await addRestaurant({
        RestaurantName: this.restaurantName,
        RestaurantIntro: this.restaurantIntro,
      });
      console.log(result);
      this.text = result.data;
      this.dialog = false;
      this.dialog2 = true;
    },
  },
};
</script>
