from django.test import TestCase
# from django.urls import reverse
from RestaurantOwner.models import Restaurants, Dishes
# Create your tests here.

class RestaurantViewGetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 3 restaurant for get tests
        creat_restaurant_objects(3)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/restaurant')
        self.assertEqual(response.status_code, 200)

    def test_default_get_method(self):
        response = self.client.get('/restaurant')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_restaurent_get_pagination(self):
        # Get second page and confirm it has (exactly) remaining 1 item
        response = self.client.get('/restaurant'+'?page=2'+'&itemsPerPage=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_restaurent_sortby_name(self):
        response = self.client.get('/restaurant' + '?sortBy=RestaurantName')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["RestaurantName"], 'a 0')

    def test_restaurent_sortby_name_desc(self):
        response = self.client.get('/restaurant' + '?sortBy=RestaurantName&sortDesc=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["RestaurantName"], 'a 2')

    def test_restaurent_sortby_id_desc(self):
        response = self.client.get('/restaurant' + '?sortBy=RestaurantId&sortDesc=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["RestaurantName"], 'a 2')

    def test_restaurent_search1(self):
        response = self.client.get('/restaurant' + '?search=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_restaurent_search2(self):
        response = self.client.get('/restaurant' + '?search=c')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

class RestaurantViewPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # For set up client in tests.
        # No data needed in this class.
        pass
        
    def test_post_successed_method(self):
        data={"RestaurantName": "Mourad","RestaurantIntro": "hoa cai"}
        # print(self.client.json_encoder)
        # self.client.json_encoder = None
        response = self.client.post('/restaurant', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Added Successfully"')

    def test_post_failed_method(self):
        data={"RestaurantName": "","RestaurantIntro": "hoa cai"}
        response = self.client.post('/restaurant', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Failed to Add"')

class RestaurantViewPutTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 1 restaurant for put tests
        creat_restaurant_objects(1)

    def test_put_succeed_method(self):
        restaurant_id = int(self.client.get('/restaurant').json()[0]["RestaurantId"])
        data={"RestaurantId": restaurant_id,"RestaurantName": "put_test","RestaurantIntro": "test"}
        response = self.client.put('/restaurant', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Updated Successfully"')
    
    def test_put_failed_method(self):
        restaurant_id = int(self.client.get('/restaurant').json()[0]["RestaurantId"])
        data={"RestaurantId": restaurant_id,"RestaurantName": "","RestaurantIntro": "test"}
        response = self.client.put('/restaurant', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Failed to Update"')
    
class RestaurantViewDeleteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 3 restaurant for delete tests
        creat_restaurant_objects(3)

    def test_delete_failed_method(self):
        restaurant_id = str(self.client.get('/restaurant').json()[0]["RestaurantId"])
        response = self.client.delete('/restaurant/' + restaurant_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Deleted Successfully"')

class DishViewGetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 12 dishes for get tests
        creat_dishes_objects(12)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/dish')
        self.assertEqual(response.status_code, 200)

    def test_default_get_method(self):
        response = self.client.get('/dish')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 12)

    def test_dish_get_pagination(self):
        # Get the third page and confirm it has (exactly) remaining 2 items
        response = self.client.get('/dish'+'?page=3'+'&itemsPerPage=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_dish_sortby_name(self):
        response = self.client.get('/dish' + '?sortBy=DishName')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["DishName"], 'a 0')

    def test_dish_sortby_name_desc(self):
        response = self.client.get('/dish' + '?sortBy=DishName&sortDesc=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["DishName"], 'a 9')

    def test_dish_sortby_rating_desc(self):
        response = self.client.get('/dish' + '?sortBy=Rating&sortDesc=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["Rating"], 5)

    def test_dish_search_word(self):
        response = self.client.get('/dish' + '?search=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_dish_search_price(self):
        response = self.client.get('/dish' + '?lowPrice=0&highPrice=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 6)

    def test_dish_search_rate(self):
        response = self.client.get('/dish' + '?lowRate=4&highRate=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)

class DishViewPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # For set up client in tests.
        # No data needed in this class.
        pass
        
    def test_post_successed_method(self):
        data={"DishName": "Shortrib","Restaurant": "Mourad","Taste": "Salty","Price":160,"Rating":5}
        # print(self.client.json_encoder)
        # self.client.json_encoder = None
        response = self.client.post('/dish', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Added Successfully"')

    def test_post_failed_method(self):
        data={"DishName": "","Restaurant": "Mourad","Taste": "Salty","Price":160,"Rating":5}
        response = self.client.post('/dish', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Failed to Add"')

class DishViewPutTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 1 dish for put tests
        creat_dishes_objects(1)

    def test_put_succeed_method(self):
        dish_id = int(self.client.get('/dish').json()[0]["DishId"])
        data={"DishId": dish_id,"DishName": "Shortrib","Restaurant": "Mourad","Taste": "Salty","Price":160,"Rating":5}
        response = self.client.put('/dish', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Updated Successfully"')
    
    def test_put_failed_method(self):
        dish_id = int(self.client.get('/dish').json()[0]["DishId"])
        data={"DishId": dish_id,"DishName": "","Restaurant": "Mourad","Taste": "Salty","Price":160,"Rating":5}
        response = self.client.put('/dish', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Failed to Update"')
    
class DishViewDeleteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 1 dishes for delete tests
        creat_dishes_objects(1)

    def test_delete_failed_method(self):
        dish_id = int(self.client.get('/dish').json()[0]["DishId"])
        response = self.client.delete('/dish/' + str(dish_id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"Deleted Successfully"')


def creat_restaurant_objects(number_of_restaurant):
    for restaurant_id in range(number_of_restaurant):
        Restaurants.objects.create(
            RestaurantName = f'a {restaurant_id}',
            RestaurantIntro = f'b {restaurant_id}',
        )


def creat_dishes_objects(number_of_dishes):
    for dish_id in range(number_of_dishes):
        Dishes.objects.create(
            DishName = f'a {dish_id}',
            Restaurant = f'b {dish_id}',
            Taste = f'c {dish_id}',
            Price = int(dish_id),
            Rating = (int(dish_id) % 5) + 1,
        )