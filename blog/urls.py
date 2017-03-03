from django.conf.urls import url
from django.views.generic import TemplateView

from . import feeds
from . import views

urlpatterns = [
    url(r'^post/(?P<slug>[\w-]+)/$', views.article, name='article'),
    url(r'^feed/$', feeds.ArticleFeed(), name='article-feed'),

    url(r'^category/(?P<slug>[\w-]+)/feed/$', feeds.CategoryFeed(), name='category-feed'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.category, name='category'),
    url(r'^category/$', views.category, name='category'),

    url(r'^tag/(?P<slug>[\w-]+)/feed/$', feeds.TagFeed(), name='tag-feed'),
    url(r'^tag/(?P<slug>[\w-]+)/$', views.tag, name='tag'),
    url(r'^tag/$', views.tag, name='tag'),

    url(r'^search/$', views.search, name='search'),

    url(r'^about/$', TemplateView.as_view(template_name='blog/about.html'), name='about'),


    url(r'^$', views.article, name='home'),
]
