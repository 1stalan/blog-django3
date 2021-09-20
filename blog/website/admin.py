from django.contrib import admin
from django.db import models
from django.db.models.base import Model
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'categories', 'deleted']
    search_fields = ['title', 'sub_title', 'categories']
    
    def get_queryset(self, request):
        return Post.objects.filter(deleted=False)


admin.site.register(Post, PostAdmin)
