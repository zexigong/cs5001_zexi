from django.test import TestCase
# from django.urls import reverse
from RestaurantOwner.models import Restaurants, Courses, Dishes
# Create your tests here.

class RestaurantViewGetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 3 restaurant for pagination tests
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


def creat_restaurant_objects(number_of_restaurant):
    for restaurant_id in range(number_of_restaurant):
        Restaurants.objects.create(
            RestaurantName = f'a {restaurant_id}',
            RestaurantIntro = f'b {restaurant_id}',
        )