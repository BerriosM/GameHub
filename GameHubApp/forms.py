from django import forms
from decimal import Decimal
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
    platform = forms.ChoiceField(
        choices=PLATFORM_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Plataforma'
    )
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Género'
    )
    price = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        min_value=0,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        label='Precio'
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label='Imagen'
    )

    class Meta:
        model = Game
        fields = ['title', 'platform', 'genre', 'description', 'price', 'image']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del juego'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Descripción'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price in [None, '']:
            return Decimal('0.00')
        return price


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'image', 'content']
        labels = {
            'title': 'Título de la noticia',
            'category': 'Categoría',
            'image': 'Imagen',
            'content': 'Contenido',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la noticia'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Contenido completo'}),
        }

    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'title', 'rating', 'image', 'content']
        labels = {
            'game': 'Juego',
            'title': 'Título de la reseña',
            'rating': 'Puntuación',
            'image': 'Imagen',
            'content': 'Contenido',
        }
        widgets = {
            'game': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la reseña'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '5'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Contenido completo'}),
        }

    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # only request comment content from the user; name will be set server-side
        fields = ['content']
        labels = {
            'content': 'Comentario',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu comentario...'})
        }
