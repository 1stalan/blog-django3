from django.urls import path, include
from .views import hello_blog
from .views import post_detail, save_form




app_name = 'blog'

urlpatterns = [
    path('', hello_blog, name='home'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('save-form/', save_form, name='save_form'),
] 