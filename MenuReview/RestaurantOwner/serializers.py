'''
convert types or model instances into native python data types.
'''
from rest_framework import serializers
from RestaurantOwner.models import Restaurants, Courses, Dishes

class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurants
        fields=('RestaurantId','RestaurantName','RestaurantIntro')