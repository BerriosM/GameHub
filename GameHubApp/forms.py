from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'platform', 'genre', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del juego'}),
            'platform': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plataforma (PS5, Xbox, PC...)'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Género'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Descripción'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre de imagen (ej. 2.jpg) en static/img/games/"}),
        }
