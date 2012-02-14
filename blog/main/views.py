from django.shortcuts import render_to_response, redirect
from django.views.decorators.cache import cache_page
from django.template import RequestContext
from main.models import Article
from main.forms import ArticleForm


#@cache_page(60 * 15)
def home(request):
    articles = Article.objects.all()
    return render_to_response('home.html', {
        'articles': articles,
    })


#@cache_page(60 * 15)
def show_article(request, pk):
    article = Article.objects.get(pk=pk)
    return render_to_response('show_article.html', {
        'article': article,
    })


def add_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_article.html', {
        'form': form,
    }, RequestContext(request))
