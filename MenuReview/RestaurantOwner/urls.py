from django.urls import re_path
from RestaurantOwner import views


urlpatterns=[
    re_path(r'^restaurant$',views.restaurantApi),
    re_path(r'^restaurant/([0-9]+)$',views.restaurantApi),
    re_path(r'^course$',views.courseApi),
    re_path(r'^course/([0-9]+)$',views.courseApi),
    re_path(r'^dish$',views.dishApi),
    re_path(r'^dish/([0-9]+)$',views.dishApi)
]