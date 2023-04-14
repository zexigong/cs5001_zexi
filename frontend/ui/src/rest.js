import axios from "axios";

export async function getRestaurants() {
  return await axios.get("http://127.0.0.1:8000/restaurant");
}

export async function addRestaurant(data) {
  return await axios.post("http://127.0.0.1:8000/restaurant", data);
}
