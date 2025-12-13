from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import News_post

class News_PostForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'name', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Полное описание новости', 'rows': 10}),
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя автора'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }



