from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('todo/', views.todo_list, name='todo'),
    path('game/', views.guess_number, name='game'),
    
]