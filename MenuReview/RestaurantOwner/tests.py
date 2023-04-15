from django.test import TestCase
from django.urls import reverse
from RestaurantOwner.models import Restaurants, Courses, Dishes
# Create your tests here.

class RestaurantViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_restaurant = 3

        for restaurant_id in range(number_of_restaurant):
            Restaurants.objects.create(
                RestaurantName = f'a {restaurant_id}',
                RestaurantIntro = f'b {restaurant_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/restaurant')
        self.assertEqual(response.status_code, 200)

    def test_default_get_method(self):
        response = self.client.get('/restaurant')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    # def test_lists_all_authors(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     response = self.client.get(reverse('authors')+'?page=2')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertEqual(len(response.context['author_list']), 3)