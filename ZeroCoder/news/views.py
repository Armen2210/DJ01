from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_PostForm
# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = News_PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неправильно'
    form = News_PostForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})
