from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('games/', views.games, name='games'),
    path('games/add/', views.AddGameView.as_view(), name='games_add'),
    path('game-single/<int:pk>/', views.game_single, name='game_single'),
    path('review/', views.review, name='review'),
    path('review/add/', views.AddReviewView.as_view(), name='review_add'),
    path('blog/', views.blog, name='blog'),
    path('blog/add/', views.AddNewsView.as_view(), name='blog_add'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('contact/', views.contact, name='contact'),
]