from tkinter import FALSE
from django.db import models


class Food(models.Model):
    food_id = models.CharField(max_length=64, blank=True)
    """ Unique food id """

    food_name = models.CharField(max_length=64)
    """ Food Name """
    food_image = models.ImageField(null=True, blank=True, upload_to="images/")

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


class Orders(models.Model):
    order_no = models.IntegerField()
    """ a unique integer of 124 length to give each order a unique id """

    order_date = models.DateTimeField()
    """ Date and Time of ordering food """

    order_items = models.JSONField()
    """ A JSON containing the list of food items ordered along with their quanity and price """

    order_tax_amount = models.IntegerField()
    """ Amount of tax applied to the order """

    order_amount = models.IntegerField()
    """ Total amount including tax, without discount """

    order_offer_applied = models.BooleanField(default=FALSE)
    """ Boolean value stating whether an offer was applied """

    order_offer_name = models.CharField(max_length=40)
    """ Name of the offer if appliend """

    order_discount_amount = models.IntegerField()
    """ Amount discounted from the order """

    order_billed_amount = models.IntegerField()
    """ Total amount billed to the order submitter """

    order_submitter_name = models.CharField(max_length=255)
    """ Name of the order submitter """

    order_payment_method = models.CharField(max_length=124)
    """ 
    Mode of payment\n
    Example:\n
    Card-Visa or Card-Mastercard
    """

    order_medium = models.CharField(max_length=40)
    """ Order medium """

# Create your models here.
