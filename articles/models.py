from django.db import models

class Category (models.Model):
    name = models.CharField( max_length=50)
    thumb = models.ImageField()

    def __str__(self):
        return self.name
    
# Create your models here.
class Article (models.Model):
    title = models.CharField( max_length=50 ,blank=True)
    slug = models.SlugField()
    categorys = models.ManyToManyField("Category")
    body = models.TextField()
    date = models.DateTimeField(  auto_now_add=True)
    thumb = models.ImageField()
    views = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
