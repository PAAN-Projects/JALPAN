from django.db import models

class Food(models.Model):
    foodName = models.CharField(max_length=255)
# Create your models here.
