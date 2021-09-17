from django.contrib import admin
from django.db import models
from django.db.models.base import Model
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name']
    search_fields = ['title', 'sub_title', 'full_name']
    


admin.site.register(Post, PostAdmin)
