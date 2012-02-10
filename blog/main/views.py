from django.shortcuts import render_to_response
from main.models import Article


def home(request):
    articles = Article.objects.all()
    return render_to_response('home.html', {
        'articles': articles,
    })


def show_article(request, pk):
    article = Article.objects.get(pk=pk)
    return render_to_response('show_article.html', {
        'article': article,
    })
