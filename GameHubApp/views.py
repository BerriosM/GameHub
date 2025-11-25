from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import CreateView as GenericCreateView
from django.http import HttpResponseForbidden

from .models import Game, BlogPost, Review, Comment
from django.contrib.auth import get_user_model
from django.db.models import Avg
from .forms import GameForm, BlogPostForm, ReviewForm, CommentForm


# Login
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Create your views here.
def main(request):
    # show latest 3 blog posts on the homepage
    posts = BlogPost.objects.order_by('-created_at')[:3]
    # latest game to feature on the homepage
    latest_game = Game.objects.order_by('-created_at').first()
    return render(request, 'index.html', {'posts': posts, 'latest_game': latest_game})

def games(request):
    # support optional filtering by genre and/or platform via query params
    genre = request.GET.get('genre')
    platform = request.GET.get('platform')
    q = request.GET.get('q')
    games = Game.objects.order_by('-created_at')
    if genre:
        games = games.filter(genre=genre)
    if platform:
        games = games.filter(platform=platform)
    if q:
        games = games.filter(title__icontains=q)
    return render(request, 'games.html', {'games': games, 'current_genre': genre, 'current_platform': platform, 'current_q': q})

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

# Add game view
class AddGameView(LoginRequiredMixin, GenericCreateView):
    model = Game
    form_class = GameForm
    template_name = "add_game.html"
    success_url = reverse_lazy('games')

    def form_valid(self, form):
        # assign current user as author and let the base class save the object
        form.instance.author = self.request.user
        return super().form_valid(form)

def review(request):
    reviews = Review.objects.order_by('-created_at')
    return render(request, 'review.html', {'reviews': reviews})


class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = reverse_lazy('review')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def blog(request):
    # support optional filtering by category via ?category=CategoriaName
    category = request.GET.get('category')
    if category:
        posts = BlogPost.objects.filter(category=category).order_by('-created_at')
    else:
        posts = BlogPost.objects.order_by('-created_at')
    latest_comments = Comment.objects.select_related('post').order_by('-created_at')[:4]
    return render(request, 'blog.html', {'posts': posts, 'latest_comments': latest_comments, 'current_category': category})

def post_single(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_single', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'post-single.html', {'post': post, 'comments': comments, 'form': form})


def review_single(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'review-single.html', {'review': review})

class AddNewsView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'add_news.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def profile(request):
    user = request.user
    user_games = Game.objects.filter(author=user).order_by('-created_at')
    user_reviews = Review.objects.filter(author=user).order_by('-created_at')
    user_posts = BlogPost.objects.filter(author=user).order_by('-created_at')
    return render(request, 'profile.html', {
        'profile_user': user,
        'user_games': user_games,
        'user_reviews': user_reviews,
        'user_posts': user_posts,
        'is_owner': True,
    })


@login_required
def user_profile(request, username):
    """View another user's profile. Renders the same `profile.html` template but with
    `profile_user` set to the requested user and `is_owner` False when the viewer is different.
    """
    User = get_user_model()
    profile_user = get_object_or_404(User, username=username)
    user_games = Game.objects.filter(author=profile_user).order_by('-created_at')
    user_reviews = Review.objects.filter(author=profile_user).order_by('-created_at')
    user_posts = BlogPost.objects.filter(author=profile_user).order_by('-created_at')
    is_owner = (request.user == profile_user)
    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'user_games': user_games,
        'user_reviews': user_reviews,
        'user_posts': user_posts,
        'is_owner': is_owner,
    })



def contact(request):
    return render(request, 'contact.html')


@login_required
def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if game.author != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este juego.")
    if request.method == 'POST':
        game.delete()
        return redirect('profile')
    return render(request, 'confirm_delete.html', {'object': game, 'type': 'juego'})


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.author != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta reseña.")
    if request.method == 'POST':
        review.delete()
        return redirect('profile')
    return render(request, 'confirm_delete.html', {'object': review, 'type': 'reseña'})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta publicación.")
    if request.method == 'POST':
        post.delete()
        return redirect('profile')
    return render(request, 'confirm_delete.html', {'object': post, 'type': 'publicación'})
