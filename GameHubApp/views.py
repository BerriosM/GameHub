from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import CreateView as GenericCreateView

from .models import Game
from .forms import GameForm


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
    return render(request, 'index.html')

def games(request):
    games = Game.objects.order_by('-created_at')
    return render(request, 'games.html', {'games': games})

def review(request):
    return render(request, 'review.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def game_single(request):
    return render(request, 'game-single.html')

