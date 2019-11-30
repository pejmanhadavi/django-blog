from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from core import models

def index(request):
    
    articles = models.Article.objects.all()
    categories = models.Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'index.html', context)



def article(request, slug):
    article = get_object_or_404(models.Article, slug=slug)
    context = {
        'article': article,
    }
    return render(request, 'article.html', context)


def category(request, slug):
    category = get_object_or_404(models.Category, slug=slug)
    articles = get_list_or_404(models.Article, category=category.id)
    categories = models.Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'index.html', context)