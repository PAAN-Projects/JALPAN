from django.db import models


class Food(models.Model):
    food_name = models.CharField(max_length=255)
    food_catagory = models.CharField(max_length=255)
