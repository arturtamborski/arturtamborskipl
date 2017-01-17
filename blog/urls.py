from django.conf.urls import url 
from . import views as blog

urlpatterns = [
    url(r'^category/(?P<slug>[\w-]+)/$', blog.category, name='category'),
    url(r'^category/$', blog.category, name='category'),
    url(r'^(?P<slug>[\w-]+)/$', blog.article, name='article'),
    url(r'^$', blog.home, name='home'),
]
