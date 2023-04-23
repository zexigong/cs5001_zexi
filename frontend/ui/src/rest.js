import axios from "axios";

const base_url = "http://127.0.0.1:8000/";

export async function getRestaurants(params) {
  if (!params) return await axios.get(base_url + "restaurant");
  return await axios.get(base_url + "restaurant", { params });
  //   return await axios.get(base_url + "restaurant");
}

export async function addRestaurant(data) {
  return await axios.post(base_url + "restaurant", data);
}

export async function deleteRestaurant(data) {
  return await axios.delete(base_url + "restaurant" + "/" + data);
}

export async function updateRestaurant(data) {
  return await axios.put(base_url + "restaurant", data);
}

export async function getDishes() {
  return await axios.get(base_url + "dish");
}

export async function addDishes(data) {
  return await axios.post(base_url + "dish", data);
}
