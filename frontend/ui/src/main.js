import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import Restaurant from "@/components/Restaurant.vue";

const routes = [
  { path: "/", component: HelloWorld, name: "home" },
  { path: "/restaurant", component: Restaurant, name: "restaurant" },
  // { path: "/menu", component: menu, name: "menu" },
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
}).$mount("#app");
