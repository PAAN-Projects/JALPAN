from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Food
import string
import random


def index(request):
    foodList = Food.objects.all().values()
    template = loader.get_template("main.html")
    context = {
        'foodList': foodList
    }
    return HttpResponse(template.render(context, request))


def addFood(request):
    template = loader.get_template('addFood.html')
    return HttpResponse(template.render({}, request))


def addFoodRecord(request):
    foodId = str(''.join(random.choices(
        string.ascii_uppercase + string.digits, k=64)))
    foodName = request.POST['foodName']
    foodCatagory = request.POST['foodCatagory']
    foodSpicy = request.POST['isFoodSpicy']
    foodPrice = request.POST['foodPrice']
    foodDesc = request.POST['foodDesc']
    foodImage = request.FILES['foodImage']

    food = Food(food_id=foodId, food_image=foodImage, food_name=foodName, food_catagory=foodCatagory,
                food_is_spicy=foodSpicy, food_price=foodPrice,
                food_desc=foodDesc)
    food.save()
    return HttpResponseRedirect(reverse('management'))


def removeFood(request, food_id):
    food = Food.objects.filter(food_id=food_id)
    food.delete()
    return HttpResponseRedirect(reverse('manage_food'))


def manageFood(request):
    template = loader.get_template("manageFood.html")
    return HttpResponse(template.render({}, request))


def editFood(request, nfoodId, nfoodName, nfoodCatagory, nfoodIsSpicy, nfoodPrice, nfoodDesc):
    template = loader.get_template("editFood.html")

    context = {
        "foodId": nfoodId,
        "foodName": nfoodName,
        "foodCatagory": nfoodCatagory,
        "foodIsSpicy": nfoodIsSpicy,
        "foodPrice": nfoodPrice,
        "foodDesc": nfoodDesc
    }
    return HttpResponse(template.render(context, request))


def editFoodRecord(request):
    foodId = request.POST['foodId']
    foodName = request.POST['foodName']
    foodCatagory = request.POST['foodCatagory']
    foodSpicy = request.POST['isFoodSpicy']
    foodPrice = request.POST['foodPrice']
    foodDesc = request.POST['foodDesc']
    food = Food.objects.get(food_id=foodId)
    try:
        foodImage = request.FILES['foodImage']
    except:
        f = food.values()
        foodImage = f[0]["food_image"]

    print(foodImage)
    food.food_id = foodId
    food.food_image = foodImage
    food.food_name = foodName
    food.food_catagory = foodCatagory
    food.food_is_spicy = foodSpicy
    food.food_price = foodPrice
    food.food_desc = foodDesc

    food.save()

    return HttpResponseRedirect(reverse("manage_food"))
