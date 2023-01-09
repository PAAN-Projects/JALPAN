from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="management"),
    path("food/add", views.addFood, name="add_food"),
    path("food/add/save", views.addFoodRecord, name="save_food"),
    path("food/manage", views.manageFood, name="manage_food"),
    path("food/remove/<str:food_id>", views.removeFood, name="remove_food"),
    path("food/edit/<str:nfoodId>/<str:nfoodName>/<str:nfoodCatagory>/<int:nfoodPrice>/<str:nfoodIsSpicy>/<str:nfoodDesc>",
         views.editFood, name="edit_food"),
    path("food/edit/save", views.editFoodRecord, name="edit_food_record"),
    path("orders/records", views.orderRecords, name="orders_records"),
]
