import os
# import django

# PROJECT_NAME = 'jalpan'

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jalpan.jalpan.settings")
# django.setup()

from management.models import Food

from pathlib import Path
import random
import string
import json

dirname = os.path.dirname(os.path.realpath(__file__))

files = [
    "menus/burgers.json",
    "menus/desserts.json",
    "menus/drinks.json",
    "menus/ice-cream.json",
    "menus/pizzas.json",
    "menus/sandwiches.json"
]

foodList = []


def run():
    for FilePath in files:
        FilePath = os.path.join(dirname, FilePath)
        foodCatagory = Path(FilePath).stem
        foodCatagory = foodCatagory.capitalize()
        print("adding => ", foodCatagory, end="\n\n")
        with open(FilePath) as file:
            fileInit = json.load(file)
        for food in fileInit:
            foodId = str(''.join(random.choices(
                string.ascii_uppercase + string.digits, k=64)))
            foodName = food['name']
            foodSpicy = food['isSpicy']
            foodPrice = food['price']
            foodDesc = food['dsc']
            foodImage = food['img']
            foodList.append(Food(food_id=foodId, food_image=foodImage, food_name=foodName, food_catagory=foodCatagory,
                                 food_is_spicy=foodSpicy, food_price=foodPrice,
                                 food_desc=foodDesc))

    objs = Food.objects.bulk_create(foodList)
