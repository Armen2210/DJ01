from .models import News_post
from django.forms import ModelForm

class News_PostForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'name', 'pub_date']



