from . import views
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'',views.article_list, name ='article_list'),
    path(r'<slug>/',views.article_detail, name= 'article_detail'),
    path(r'category/',views.article_category, name= 'article_category')
]
