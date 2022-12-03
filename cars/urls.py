from django.urls import path
from . import views

urlpatterns = [
    path('show', views.HomePage, name='home'),
    path('', views.CarShow, name='cars'),
    path('regcar', views.RegisterCar, name='registercar'),
    path('car_details/<int:pk>', views.CarDetails, name='details'),
    path('search/', views.Search, name='search'),
    path('login/', views.LoginClient, name='login'),
    path('logout/', views.LogoutClient, name='logout'),
    path('register/', views.RegClients, name='register'),

]
