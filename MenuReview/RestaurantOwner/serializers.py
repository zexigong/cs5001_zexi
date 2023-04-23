'''
convert types or model instances into native python data types.
'''
from rest_framework import serializers
from RestaurantOwner.models import Restaurants, Dishes

class RestaurantsSerializer(serializers.ModelSerializer):
    """Convert Restaurants model instances into native python data types"""
    class Meta:
        model=Restaurants
        fields=('RestaurantId','RestaurantName','RestaurantIntro')


class DishesSerializer(serializers.ModelSerializer):
    """Convert Restaurants model instances into native python data types"""
    class Meta:
        model=Dishes
        fields=('DishId','DishName','Restaurant','Taste','Price','Rating')