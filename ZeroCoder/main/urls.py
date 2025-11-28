from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page 2'),
    path('data', views.data, name='page 3'),
    path('test', views.test, name='page 4')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)