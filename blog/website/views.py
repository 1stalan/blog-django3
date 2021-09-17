from django.shortcuts import render
from .models import Post

# Create your views here.

def hello_blog(request):
    lista_post = Post.objects.all()
    data = {"posts":lista_post}
    return render(request, 'index.html', data)