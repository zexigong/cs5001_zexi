import axios from "axios";

const base_url = "http://127.0.0.1:8000/";

export async function getRestaurants() {
  //   if (!params) return await axios.get(base_url + "restaurant");
  //   return await axios.get(base_url + "restaurant", { params });
  return await axios.get(base_url + "restaurant");
}

export async function addRestaurant(data) {
  return await axios.post(base_url + "restaurant", data);
}

export async function getDishes() {
  return await axios.get(base_url + "dish");
}

export async function addDishes(data) {
  return await axios.post(base_url + "dish", data);
}
