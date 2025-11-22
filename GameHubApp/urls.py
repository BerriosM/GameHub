from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('games/', views.games, name='games'),
    path('games/add/', views.AddGameView.as_view(), name='games_add'),
    path('review/', views.review, name='review'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('game-single/', views.game_single, name='game_single'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]