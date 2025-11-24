from django import forms
from .models import Game
from .models import BlogPost
from .models import Review
from .models import Comment


# Opciones por defecto — puedes modificarlas a tu gusto
PLATFORM_CHOICES = [
    ('PC', 'PC'),
    ('PS5', 'PS5'),
    ('PS4', 'PS4'),
    ('Xbox Series X', 'Xbox Series X'),
    ('Xbox One', 'Xbox One'),
    ('Nintendo Switch', 'Nintendo Switch'),
    ('Nintendo Switch 2', 'Nintendo Switch 2'),
]

GENRE_CHOICES = [
    ('Accion', 'Accion'),
    ('Aventura', 'Aventura'),
    ('Carreras', 'Carreras'),
    ('Disparos', 'Disparos'),
    ('Estrategia', 'Estrategia'),
    ('RPG', 'RPG'),
    ('Deportes', 'Deportes'),
]


class GameForm(forms.ModelForm):
    # Reemplazamos los inputs de texto por selects
    platform = forms.ChoiceField(choices=PLATFORM_CHOICES,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    genre = forms.ChoiceField(choices=GENRE_CHOICES,
                              widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Game
        fields = ['title', 'platform', 'genre', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del juego'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Descripción'}),
        }


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'image', 'excerpt', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la noticia'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ruta imagen (p.ej. img/blog-big/1.jpg)"}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Extracto corto'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Contenido completo'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'title', 'rating', 'image', 'excerpt', 'content']
        widgets = {
            'game': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la reseña'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '5'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ruta imagen (p.ej. img/review/1.jpg)'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Extracto corto'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Contenido completo'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre (opcional)'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu comentario...'}),
        }
