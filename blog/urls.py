from django.conf.urls import url 
from . import views as blog

urlpatterns = [
    url(r'^category/(?P<slug>[\w-]+)/$', blog.category, name='category'),
    url(r'^category/$', blog.category, name='category'),

    url(r'^article/(?P<slug>[\w-]+)/$', blog.article, name='article'),
    url(r'^article/$', blog.article, name='article'),

    url(r'^search/$', blog.search, name='search'),

    url(r'^meta/$', blog.meta, name='meta'),

    url(r'^$', blog.home, name='home'),
]
