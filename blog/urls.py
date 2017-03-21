from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import feeds
from . import views

urlpatterns = [
    url(r'^comments/',                              include('django_comments.urls')),

    url(r'^posts/(?P<slug>[\w-]+)/$',               views.ArticleDetail.as_view(),  name='article'),
    url(r'^feed/$',                                 feeds.ArticleFeed(),            name='article-feed'),

    url(r'^categories/(?P<slug>[\w-]+)/feed/$',     feeds.CategoryFeed(),           name='category-feed'),
    url(r'^categories/(?P<slug>[\w-]+)/$',          views.CategoryDetail.as_view(), name='category'),
    url(r'^categories/$',                           views.CategoryList.as_view(),   name='category'),

    url(r'^tags/(?P<slug>[\w-]+)/feed/$',           feeds.TagFeed(),                name='tag-feed'),
    url(r'^tags/(?P<slug>[\w-]+)/$',                views.TagDetail.as_view(),      name='tag'),
    url(r'^tags/$',                                 views.TagList.as_view(),        name='tag'),


    url(r'^search/$',                               views.SearchList.as_view(),     name='search'),

    url(r'^about/$',    TemplateView.as_view(template_name='blog/about.html'),      name='about'),
    url(r'^projects/$', TemplateView.as_view(template_name='blog/projects.html'),   name='projects'),

    url(r'^$',                                      views.ArticleList.as_view(),    name='home'),
]
