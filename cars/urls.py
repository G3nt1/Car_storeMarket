from django.urls import path
from . import views

urlpatterns = [
    path('index', views.Index, name='index'),
    path('', views.CarShow, name='cars'),
    path('regcar', views.RegisterCar, name='register_car'),
    path('car_details/<int:pk>', views.CarDetails, name='details'),
    path('login/', views.LoginClient, name='login'),
    path('logout/', views.LogoutClient, name='logout'),
    path('register/', views.RegClients, name='register'),
    path('search/', views.Search, name='search'),

]
