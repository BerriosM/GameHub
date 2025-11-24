from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import CreateView as GenericCreateView

from .models import Game, BlogPost, Review
from django.db.models import Avg
from .forms import GameForm, BlogPostForm, ReviewForm


# Login
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Add game view
class AddGameView(GenericCreateView):
    model = Game
    form_class = GameForm
    template_name = "add_game.html"
    success_url = reverse_lazy('games')

# Create your views here.
def main(request):
    # show latest 3 blog posts on the homepage
    posts = BlogPost.objects.order_by('-created_at')[:3]
    return render(request, 'index.html', {'posts': posts})

def games(request):
    games = Game.objects.order_by('-created_at')
    return render(request, 'games.html', {'games': games})

def review(request):
    reviews = Review.objects.order_by('-created_at')
    return render(request, 'review.html', {'reviews': reviews})


class AddReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = reverse_lazy('review')

def blog(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})


class AddNewsView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'add_news.html'
    success_url = reverse_lazy('blog')

def contact(request):
    return render(request, 'contact.html')

def game_single(request, pk):
    game = get_object_or_404(Game, pk=pk)
    # reviews related to this game
    reviews = Review.objects.filter(game=game).order_by('-created_at')
    # calculate average rating if any
    average_rating = None
    if reviews.exists():
        avg = reviews.aggregate(Avg('rating'))
        average_rating = round(avg['rating__avg'] or 0, 1)

    return render(request, 'game-single.html', {
        'game': game,
        'reviews': reviews,
        'average_rating': average_rating,
    })

