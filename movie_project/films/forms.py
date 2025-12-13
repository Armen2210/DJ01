from django.forms import ModelForm, TextInput, Textarea
from .models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фильма'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание фильма',
                'rows': 4
            }),
            'review': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш отзыв о фильме',
                'rows': 4
            }),
        }
