from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'index.html')

def games(request):
    return render(request, 'games.html')

def review(request):
    return render(request, 'review.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def game_single(request):
    return render(request, 'game-single.html')
