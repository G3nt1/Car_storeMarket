from cars.views import cars, authentication, messages
from django.urls import path

urlpatterns = [
    # path('index', messages.Index, name='index'),
    path('', cars.CarShow, name='cars'),
    path('advanced-search', cars.CarAdvancedSearch, name='cars_advanced_search'),
    path('regcar', cars.Register_Car, name='register_car'),
    path('update-car/<int:pk>', cars.Update_Car, name='update_car'),
    path('car_details/<int:pk>', cars.CarDetails, name='details'),
    path('profile/<int:pk>', authentication.Profile, name='profile'),
    path('login/', authentication.LoginClient, name='login'),
    path('logout/', authentication.LogoutClient, name='logout'),
    path('register/', authentication.RegClients, name='register'),
    path('messages/', messages.Index, name='messages_index'),
    path('messages/<str:username>', messages.Index, name='messages_from_user'),

]
