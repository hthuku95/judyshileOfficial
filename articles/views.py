from django.shortcuts import render
from .models import Article ,Category

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.htm',{'articles':articles})


def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    article.views = article.views + 1
    article.save()
    return render(request,'articles/article_detail.htm',{'article':article})

def article_category(request):
    categorys = Category.objects.all()
    return render(request,'articles/article_category.htm',{'categorys':categorys})
    

