from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from RestaurantOwner.models import Restaurants, Dishes
from RestaurantOwner.serializers import RestaurantsSerializer, DishesSerializer

# Create your views here.


def pagination(object_list,request):
    """Pagination function seperating data into different pages.
    Return a certain page of data that satisfied the request."""
    page = int(request.GET.get('page', 1))
    items_per_page = int(request.GET.get('itemsPerPage', 100))
    if items_per_page == -1:
        items_per_page = 1000
    return object_list[(page-1)*items_per_page:page*items_per_page]


def sort(object_list,request,default):
    """Sort the data by a requested parameter or the default parameter
      in asceding or desdending order. Return the sorted object list."""
    sort_by = request.GET.get('sortBy', default)
    sort_desc = (request.GET.get('sortDesc', 'false') == 'true')
    if sort_desc:
        return object_list.order_by('-' + sort_by).values()
    return object_list.order_by(sort_by).values()


def search_restaurant(object_list,key_word):
    """Search and return all restaurant objects that contains the key_word.
    key_word is case insensitive."""
    res = object_list.filter(RestaurantName__icontains=key_word).values() | object_list.filter(RestaurantIntro__icontains=key_word).values()
    return res


def search_dish_word(object_list,key_word):
    """Search and return all dish objects that contains the key_word.
    key_word is case insensitive."""
    res = object_list.filter(DishName__icontains=key_word).values() | object_list.filter(Restaurant__icontains=key_word).values() | object_list.filter(Taste__icontains=key_word).values()
    return res


def search_dish_price(object_list,lower,upper):
    """Search and return all dish objects whose price are between lower and upper."""
    res = object_list.filter(Price__gte=lower, Price__lte=upper).values()
    return res


def search_dish_rating(object_list,lower,upper):
    """Search and return all dish objects whose rating are between lower and upper."""
    res = object_list.filter(Rating__gte=lower, Rating__lte=upper).values()
    return res


@csrf_exempt
def restaurantApi(request,id=0):
    """This is the restaurantApi function.
    This function take in the website request and return the coresponding response."""
    if request.method == 'GET':
        # get restaurants data from database and return the requested data.
        restaurants = Restaurants.objects.all()
        key_word = request.GET.get('search')
        if key_word:
            restaurants = search_restaurant(restaurants, key_word)
        restaurants_num = len(restaurants)
        restaurants_sort = sort(restaurants,request, "RestaurantId")
        restaurants_page = pagination(restaurants_sort,request)
        restaurants_serializer = RestaurantsSerializer(restaurants_page,many=True)
        return JsonResponse({'itemsNum': restaurants_num, 'data':restaurants_serializer.data},safe=False)
    elif request.method == 'POST':
        # Add new restaurant object to database.
        restaurants_data = JSONParser().parse(request)
        restaurants_serializer=RestaurantsSerializer(data=restaurants_data)
        if restaurants_serializer.is_valid():
            restaurants_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method == 'PUT':
        # Update a particular restaurant object.
        restaurants_data = JSONParser().parse(request)
        restaurant = Restaurants.objects.get(RestaurantId=restaurants_data['RestaurantId'])
        restaurants_serializer=RestaurantsSerializer(restaurant,data=restaurants_data)
        if restaurants_serializer.is_valid():
            restaurants_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update',safe=False)
    elif request.method == 'DELETE':
        # Delete a particular restaurant object.
        restaurant = Restaurants.objects.get(RestaurantId=id)
        restaurant.delete()
        return JsonResponse('Deleted Successfully',safe=False)
    

@csrf_exempt
def dishApi(request,id=0):
    """This is the dishApi function.
    This function take in the website request and return the coresponding response."""
    if request.method == 'GET':
        # get dishes data from database and return the requested data.
        dishes = Dishes.objects.all()
        key_word = request.GET.get('search')
        lower_price, upper_price = request.GET.get('lowPrice', 0), request.GET.get('highPrice', 99999)
        lower_rate, upper_rate = request.GET.get('lowRate', 1), request.GET.get('highRate', 5)
        if key_word:
            dishes = search_dish_word(dishes, key_word)
        dishes_num = len(dishes)
        dishes = search_dish_price(dishes, lower_price, upper_price)
        dishes = search_dish_rating(dishes, lower_rate, upper_rate)
        dishes_sort = sort(dishes,request, "DishId")
        dishes_page = pagination(dishes_sort,request)
        dishes_serializer=DishesSerializer(dishes_page,many=True)
        return JsonResponse({'itemsNum': dishes_num, 'data':dishes_serializer.data},safe=False)
    elif request.method == 'POST':
        # Add new dish object to database.
        dishes_data = JSONParser().parse(request)
        dishes_serializer=DishesSerializer(data=dishes_data)
        if dishes_serializer.is_valid():
            dishes_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method == 'PUT':
        # Update a particular dish object.
        dishes_data = JSONParser().parse(request)
        dishes = Dishes.objects.get(DishId=dishes_data['DishId'])
        dishes_serializer=DishesSerializer(dishes,data=dishes_data)
        if dishes_serializer.is_valid():
            dishes_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update',safe=False)
    elif request.method == 'DELETE':
        # Delete a particular dish object.
        dishes = Dishes.objects.get(DishId=id)
        dishes.delete()
        return JsonResponse('Deleted Successfully',safe=False)
