from django.conf.urls import url
from django.views.generic import TemplateView

from . import feeds
from . import views

urlpatterns = [
    url(r'^feed/$', feeds.PostRssFeed(), name='post-rss-feed'),
    url(r'^rss/$', feeds.PostRssFeed(), name='post-rss-feed'),
    url(r'^atom/$', feeds.PostAtomFeed(), name='post-atom-feed'),

    url(r'^post/(?P<slug>[\w-]+)/$', views.article, name='article'),

    url(r'^category/(?P<slug>[\w-]+)/feed/$', feeds.CategoryRssFeed(), name='category-rss-feed'),
    url(r'^category/(?P<slug>[\w-]+)/rss/$', feeds.CategoryRssFeed(), name='category-rss-feed'),
    url(r'^category/(?P<slug>[\w-]+)/atom/$', feeds.CategoryAtomFeed(), name='category-atom-feed'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.category, name='category'),
    url(r'^category/$', views.category, name='category'),

    url(r'^tag/(?P<slug>[\w-]+)/feed/$', feeds.TagRssFeed(), name='tag-rss-feed'),
    url(r'^tag/(?P<slug>[\w-]+)/rss/$', feeds.TagRssFeed(), name='tag-rss-feed'),
    url(r'^tag/(?P<slug>[\w-]+)/atom/$', feeds.TagAtomFeed(), name='tag-atom-feed'),
    url(r'^tag/(?P<slug>[\w-]+)/$', views.tag, name='tag'),
    url(r'^tag/$', views.tag, name='tag'),

    url(r'^search/$', views.search, name='search'),

    url(r'^about/$', TemplateView.as_view(template_name='blog/about.html'), name='about'),

    url(r'^$', views.article, name='home'),
]
