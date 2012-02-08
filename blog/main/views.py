from django.shortcuts import render_to_response
from main.models import Article


def home(request):
    articles = Article.objects.all()
    return render_to_response('home.html', {
        'articles': articles,
    })
