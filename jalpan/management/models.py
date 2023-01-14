from django.db import models


class Food(models.Model):
    food_id = models.CharField(max_length=64, blank=True)
    """ Unique food id """

    food_name = models.CharField(max_length=64)
    """ Food Name """
    food_image = models.ImageField(null=True, blank=True, upload_to="images/")
    """ Food Image """

    food_catagory = models.CharField(max_length=64)
    """ 
    Food Catagories.\n
    Example:\n
    Thai, Chinese, Indian, Multicuisine
    """

    food_is_spicy = models.BooleanField()
    """ Is food spicy """

    food_price = models.IntegerField()
    """ Price of food """

    food_desc = models.CharField(max_length=205)
