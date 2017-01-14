from django.contrib.sitemaps.views import sitemap
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('blog.urls')),
    url(r'^blog', include('blog.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
