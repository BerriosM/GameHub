from django import forms
from .models import Game


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
