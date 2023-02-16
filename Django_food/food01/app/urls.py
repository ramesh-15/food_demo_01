from django.urls import path
from . import  views

urlpatterns =[
    path('',views.NGOHome,name='NGOHome'),
    path('NGOHome',views.NGOHome,name='NGOHome'),
    path('FoodRequest/<int:id>',views.FoodRequest,name='FoodRequest'),
    path('Cart_NGO',views.Cart_NGO,name='Cart_NGO'),
    path('FoodCancel/<int:food_id>',views.FoodCancel,name='FoodCancel'),
]