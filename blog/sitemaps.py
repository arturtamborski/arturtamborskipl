from django.contrib.sitemaps import Sitemap
from . import models

class ArticleSitemap(Sitemap):
    changefreq = 'never'
    protocol = 'https'
    priority = 0.5

    def items(self):
        return models.Article.objects.published()

    def lastmod(self, obj):
        return obj.date
