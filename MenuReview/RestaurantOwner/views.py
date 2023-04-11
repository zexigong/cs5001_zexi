from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RestaurantOwner.models import Restaurants, Courses, Dishes
from RestaurantOwner.serializers import RestaurantsSerializer, CoursesSerializer, DishesSerializer

# Create your views here.

@csrf_exempt
def restaurantApi(request,id=0):
    if request.method == 'GET':
        restaurants = Restaurants.object.all()
        restaurants_serializer=RestaurantsSerializer(restaurants,many=True)
        return JsonResponse(restaurants_serializer.data,safe=False)
    elif request.method == 'POST':
        restaurants_data = JSONParser().parse(request)
        restaurants_serializer=RestaurantsSerializer(data=restaurants_data)
        if restaurants_serializer.is_valid():
            restaurants_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method == 'PUT':
        restaurants_data = JSONParser().parse(request)
        restaurant = Restaurants.object.get(RestaurantId=restaurants_data['RestaurantId'])
        restaurants_serializer=RestaurantsSerializer(restaurant,data=restaurants_data)
        if restaurants_serializer.is_valid():
            restaurants_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update',safe=False)
    elif request.method == 'DELETE':
        restaurant = Restaurants.object.get(RestaurantId=id)
        restaurant.delete()
        return JsonResponse('Deleted Successfully',safe=False)