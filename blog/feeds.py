from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy

from . import models

class ArticleFeed(Feed):
    title = 'Latest posts from my blog.'
    link  = reverse_lazy('home')

    def items(self):
        return models.Article.objects.published()

    def item_description(self, item):
        return item.content_html[:200]

    def item_pubdate(self, item):
        return item.date


class CategoryFeed(Feed):
    def title(self, item):
        return 'Latest posts from category: ' + item.name

    def link(self, item):
        return item.get_absolute_url()

    def get_object(self, request, slug):
        return models.Category.objects.get(slug=slug)

    def items(self, item):
        return models.Article.objects.published().filter(category=item)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content_html[:200]

    def item_pubdate(self, item):
        return item.date

    def item_link(self, item):
        return item.get_absolute_url()


class TagFeed(Feed):
    def title(self, item):
        return 'Latest posts from tag: ' + item.name

    def link(self, item):
        return item.get_absolute_url()

    def get_object(self, request, slug):
        return models.Tag.objects.get(slug=slug)

    def items(self, item):
        return models.Article.objects.published().filter(tags=item)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content_html[:200]

    def item_pubdate(self, item):
        return item.date

    def item_link(self, item):
        return item.get_absolute_url()
