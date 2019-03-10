from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('quests', views.quest_list, name='quest_list'),
    path('quests/<int:pk>/', views.quest, name='quest'),
]