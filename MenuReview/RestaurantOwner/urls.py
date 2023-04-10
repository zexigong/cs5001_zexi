from django.conf.urls import url
from RestaurantOwner import views


urlpatterns=[
    url(r'^restaurant$',views.departmentApi),
    url(r'^restaurant/([0-9]+)$',views.departmentApi)
]