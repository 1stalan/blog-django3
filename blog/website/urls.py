from django.urls import path, include
from .views import hello_blog

app_name = 'blog'

urlpatterns = [
    path('', hello_blog),
]