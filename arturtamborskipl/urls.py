from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import BlogSitemap

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': BlogSitemap}}),

    url(r'^', include('blog.urls')),
]
