from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='home'),
    url(r'^article/(?P<pk>\d+)$', 'main.views.show_article', name='show_article')
)
