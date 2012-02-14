from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'home', name='home'),
    url(r'^article/(?P<pk>\d+)$', 'show_article', name='show_article'),
    url(r'^article/add/$', 'add_article', name='add_article'),
)
