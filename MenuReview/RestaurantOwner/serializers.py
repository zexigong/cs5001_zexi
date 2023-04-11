'''
convert types or model instances into native python data types.
'''
from rest_framework import serializers
from RestaurantOwner.models import Restaurants, Courses, Dishes

class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurants
        fields=('RestaurantId','RestaurantName','RestaurantIntro')

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=('CourseId','CourseName','Restaurant','CourseDescription')

class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields=('DishId','DishName','Restaurant','Course','recipe','taste','price')