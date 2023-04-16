from django.db import models

# Create your models here.

class Restaurants(models.Model):
    RestaurantId = models.AutoField(primary_key=True)
    RestaurantName = models.CharField(max_length=500)
    RestaurantIntro = models.CharField(max_length=2000)

class Courses(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=500)
    Restaurant = models.CharField(max_length=500)
    CourseDescription = models.CharField(max_length=2000)

class Dishes(models.Model):
    DishId = models.AutoField(primary_key=True)
    DishName = models.CharField(max_length=500)
    Restaurant = models.CharField(max_length=500)
    Taste = models.CharField(max_length=3000)
    Price = models.IntegerField()
    Rating = models.IntegerField()