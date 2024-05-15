
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home' ),
    path('update_task/<str:pk>/', updateTask, name = 'update_task'),
    path('delete/<str:pk>/', deleteTask, name = 'delete_task'),
    path('register/', registerPage, name = 'register'),
    path('login/', loginPage, name = 'login'),
    path('logout/', logoutPage, name = 'logout'),

]