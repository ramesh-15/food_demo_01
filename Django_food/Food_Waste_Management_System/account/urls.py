from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name = 'home'),
    path('about',views.about, name = 'about'),
    path('contact',views.contact,name = 'contact'),
    path('donar_register',views.donar_register,name = 'donar_register'),
    path('donarlogin',views.donarlogin,name = 'donarlogin'),

]
