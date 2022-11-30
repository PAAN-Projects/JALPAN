from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addFood/", views.addFood, name="addFood"),
    path("addFood/addFoodRecord/", views.addFoodRecord, name="addFoodRecord")
]