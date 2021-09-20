from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Categories(models.TextChoices):
    tech = 'TC', 'Tecnologia'
    universe = 'CR', 'Curiosidades'
    gr = 'GR', 'Geral'

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

    categories = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.gr,
    )

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + ' ' + self.sub_title
    
    full_name.admin_order_field = 'title'