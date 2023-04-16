from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RestaurantOwner.models import Restaurants, Courses, Dishes
from RestaurantOwner.serializers import RestaurantsSerializer, CoursesSerializer, DishesSerializer

# Create your views here.


def pagination(object_list,request):
    page = int(request.GET.get('page', 1))
    items_per_page = int(request.GET.get('itemsPerPage', 100))
    return object_list[(page-1)*items_per_page:page*items_per_page]


def sort(object_list,request):
    sort_by = request.GET.get('sortBy', 'RestaurantId')
    sort_desc = bool(request.GET.get('sortDesc', 0))
    if sort_desc:
        return object_list.order_by('-' + sort_by).values()
    return object_list.order_by(sort_by).values()


def search_restaurant(object_list,key_word):
    res = object_list.filter(RestaurantName__icontains=key_word).values() | object_list.filter(RestaurantIntro__icontains=key_word).values()
    return res


@csrf_exempt
def restaurantApi(request,id=0):
    restaurants = Restaurants.objects.all()
    if request.method == 'GET':
        key_word = request.GET.get('search')
        if key_word:
            restaurants = search_restaurant(restaurants, key_word)
        restaurants_sort = sort(restaurants,request)
        restaurants_page = pagination(restaurants_sort,request)
        restaurants_serializer=RestaurantsSerializer(restaurants_page,many=True)
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
        restaurant = Restaurants.objects.get(RestaurantId=restaurants_data['RestaurantId'])
        restaurants_serializer=RestaurantsSerializer(restaurant,data=restaurants_data)
        if restaurants_serializer.is_valid():
            restaurants_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update',safe=False)
    elif request.method == 'DELETE':
        restaurant = Restaurants.objects.get(RestaurantId=id)
        restaurant.delete()
        return JsonResponse('Deleted Successfully',safe=False)
    

@csrf_exempt
def courseApi(request,id=0):
    if request.method == 'GET':
        courses = Courses.objects.all()
        courses_serializer=CoursesSerializer(courses,many=True)
        return JsonResponse(courses_serializer.data,safe=False)
    elif request.method == 'POST':
        courses_data = JSONParser().parse(request)
        courses_serializer=CoursesSerializer(data=courses_data)
        if courses_serializer.is_valid():
            courses_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method == 'PUT':
        courses_data = JSONParser().parse(request)
        courses = Courses.objects.get(CourseId=courses_data['CourseId'])
        courses_serializer=CoursesSerializer(courses,data=courses_data)
        if courses_serializer.is_valid():
            courses_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update',safe=False)
    elif request.method == 'DELETE':
        print(id)
        courses = Courses.objects.get(CourseId=id)
        courses.delete()
        return JsonResponse('Deleted Successfully',safe=False)
    

@csrf_exempt
def dishApi(request,id=0):
    if request.method == 'GET':
        dishes = Dishes.objects.all()
        dishes_serializer=DishesSerializer(dishes,many=True)
        return JsonResponse(dishes_serializer.data,safe=False)
    elif request.method == 'POST':
        dishes_data = JSONParser().parse(request)
        dishes_serializer=DishesSerializer(data=dishes_data)
        if dishes_serializer.is_valid():
            dishes_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method == 'PUT':
        dishes_data = JSONParser().parse(request)
        dishes = Dishes.objects.get(DishId=dishes_data['DishId'])
        dishes_serializer=DishesSerializer(dishes,data=dishes_data)
        if dishes_serializer.is_valid():
            dishes_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update',safe=False)
    elif request.method == 'DELETE':
        dishes = Dishes.objects.get(DishId=id)
        dishes.delete()
        return JsonResponse('Deleted Successfully',safe=False)