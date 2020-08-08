from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField( max_length=50)
    thumb = models.ImageField()

    def __str__(self):
        return self.name

class Article (models.Model):
    title = models.CharField( max_length=50 ,blank=True)
    slug = models.SlugField()
    section_one = models.TextField()
    thumb_one = models.ImageField(blank=True,null=True)
    section_two = models.TextField(null=True)
    thumb_two = models.ImageField(blank=True,null=True)
    section_three = models.TextField(null=True)
    thumb_three = models.ImageField(blank=True,null=True)
    date = models.DateTimeField(  auto_now_add=True)
    thumb = models.ImageField()
    views = models.IntegerField(blank=True,default=0)
    description = models.FileField(null=True)
    category = models.ManyToManyField(Category,blank = True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.section_one[:50] 

#about and contacts
from django.db import models
class About (models.Model):
    body = models.TextField(max_length= 1024)
    image = models.ImageField()

    def snippet(self):
        return self.body[:50]

    def __str__(self):
        return self.body

class Contact (models.Model):
    firstName = models.CharField(max_length=50)
    lastname = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField()
    def __str__(self):
        return self.firstname
    

