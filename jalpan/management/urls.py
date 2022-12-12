from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="management"),
    path("food/add/", views.addFood, name="add_food"),
    path("food/add/save", views.addFoodRecord, name="save_food")
]
