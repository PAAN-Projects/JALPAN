from management.models import Food
from django import template
from django.db.models import Count
from itertools import groupby
register = template.Library()


@register.inclusion_tag("menu.html")
def menu_list():
    food_list = Food.objects.all().values()
    food_catagories = list(Food.objects.all().values_list(
        "food_catagory", flat=True).order_by().distinct())
    filtered = food_list.filter(food_catagory="Fast Food")
    sorted_food = []
    for catagory in food_catagories:
        filtered = {
            "catagory_name": catagory,
            "food_items": list(food_list.filter(food_catagory=catagory).all())
        }
        sorted_food.append(filtered)
    return {
        "RawFoodList": sorted_food
    }
