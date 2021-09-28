from django.shortcuts import render
from .models import Post, Contact

# Create your views here.


def hello_blog(request):
    lista_post = Post.objects.filter(deleted=False)
    data = {"posts": lista_post}
    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    data = {"post": post}
    return render(request, 'post_detail.html', data)


def save_form(request):
    name  = request.POST['name']
    Contact.objects.create(
        name=name,
        email=request.POST['email'],
        message=request.POST['message']
    )
    data = {"name": name}
    return render(request, 'contact.html', data)
