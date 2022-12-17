from audioop import reverse
from re import template
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Food


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
    foodName = request.POST['foodName']
    foodCatagory = request.POST['foodCatagory']
    foodSpicy = request.POST['isFoodSpicy']
    foodPrice = request.POST['foodPrice']

    food = Food(food_name=foodName, food_catagory=foodCatagory,
                food_is_spicy=foodSpicy, food_price=foodPrice)
    food.save()
    return HttpResponseRedirect(reverse('management'))


def orderRecords(request):
    template = loader.get_template("orders.html")
    return HttpResponse(template.render({}, request))
