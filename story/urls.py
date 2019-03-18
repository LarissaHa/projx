from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('quests', views.quest_list, name='quest_list'),
    path('quests/<int:pk>/', views.quest, name='quest'),
    path('player/new_player/', views.new_player, name='new_player'),
    path('player/<int:pk>/', views.detail_player, name='detail_player'),
    path('player/<int:pk>/edit_player/', views.edit_player, name='edit_player'),
    path('player', views.player_list, name='player_list'),
]