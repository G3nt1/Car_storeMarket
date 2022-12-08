from django.urls import path
from . import views

urlpatterns = [
    path('index', views.Index, name='index'),
    path('', views.CarShow, name='cars'),
    path('regcar', views.Register_Car, name='register_car'),
    path('update-car/<int:pk>', views.Update_Car, name='update_car'),
    path('car_details/<int:pk>', views.CarDetails, name='details'),
    path('login/', views.LoginClient, name='login'),
    path('logout/', views.LogoutClient, name='logout'),
    path('register/', views.RegClients, name='register'),
    path('search/', views.Search, name='search'),

]
