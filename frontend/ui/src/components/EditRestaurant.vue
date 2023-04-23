<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="888">
      <v-card>
        <v-card-title class="text-h5 grey lighten-2"> Edit Restaurant </v-card-title>
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
          <v-btn color="primary" text @click="onUpdate"> Update </v-btn>
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
import { updateRestaurant } from "@/rest";
export default {
  name: "EditRestaurant",
  props: {
    triggerEdit: {
      type: Boolean,
      default: false,
    },
    restaurantToEdit: {
      type: Object,
    },
  },

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
      restaurantId: "",
      text: "",
    };
  },
  methods: {
    async onUpdate() {
      const result = await updateRestaurant({
        RestaurantId: this.restaurantId,
        RestaurantName: this.restaurantName,
        RestaurantIntro: this.restaurantIntro,
      });
      this.text = result.data;
      this.dialog = false;
      this.dialog2 = true;
      this.$emit("fetch-data");
    },
  },
  watch: {
    triggerEdit() {
      console.log(this.restaurantToEdit);
      this.restaurantName = this.restaurantToEdit.RestaurantName;
      this.restaurantIntro = this.restaurantToEdit.RestaurantIntro;
      this.restaurantId = this.restaurantToEdit.RestaurantId;
      this.dialog = true;
    },
  },
};
</script>
