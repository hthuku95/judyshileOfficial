from django.contrib import admin

# Register your models here.
from .models import Article , Category,Contact,About
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(About)
admin.site.site_header = 'Leshi Admin'