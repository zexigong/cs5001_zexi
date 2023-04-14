import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import Home from "@/components/Home.vue";
import Restaurant from "@/components/Restaurant.vue";
import AddRestaurant from "@/components/AddRestaurant.vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import "@mdi/font/css/materialdesignicons.css";

Vue.use(Vuetify);
const vuetify = new Vuetify({});

const routes = [
  { path: "/", component: Home, name: "home" },
  { path: "/restaurant", component: Restaurant, name: "restaurant" },
  { path: "/restaurant/add", component: AddRestaurant, name: "add" },
];
Vue.use(VueRouter);

const router = new VueRouter({
  mode: "hash",
  routes,
});

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  router,
  vuetify,
}).$mount("#app");
