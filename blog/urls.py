from django.conf.urls import url
from django.views.generic import TemplateView
from . import views as blog

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', blog.article, name='article'),
    url(r'^$', blog.article, name='article'),

    url(r'^category/(?P<slug>[\w-]+)/$', blog.category, name='category'),
    url(r'^category/$', blog.category, name='category'),

    url(r'^tag/(?P<slug>[\w-]+)/$', blog.tag, name='tag'),
    url(r'^tag/$', blog.tag, name='tag'),

    url(r'^search/$', blog.search, name='search'),

    url(r'^about/$', TemplateView.as_view(template_name='blog/about.html'), name='about'),

    url(r'^$', blog.article, name='home'),
]
