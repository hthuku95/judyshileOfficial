from django.shortcuts import render
from .models import Article ,Category

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    categories = Category.objects.all()
    return render(request,'articles/article_list.htm',{'articles':articles},{'categories':categories})


def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    articles = Article.objects.filter().order_by('date')
    article.views = article.views + 1
    article.save()
    return render(request,'articles/article_detail.htm',{'article':article ,'articles':articles})


def article_category(request, slug):
    articles = Article.objects.filter(category__name = slug)
    stories = Article.objects.all()
    categories = Category.objects.all()
    return render(request,'articles/article_category.htm',{'articles':articles,'categories':categories,'stories':stories})


