from django.contrib.sitemaps.views import sitemap
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='blog/', permanent=False)),
    url(r'^blog/', include('blog.urls')),
    url(r'^adnim/', admin.site.urls),
    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
