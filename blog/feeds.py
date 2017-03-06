from django.contrib.syndication.views import Feed
from django.urls import reverse

from . import models

FEED_DESCRIPTION_MAX = 200

class ArticleFeed(Feed):
    title = 'Latest posts'
    link  = ''

    def items(self):
        return models.Article.objects.published()

    def item_description(self, item):
        if len(item.content) > FEED_DESCRIPTION_MAX:
            return item.content_html[:FEED_DESCRIPTION_MAX] + '...'
        else:
            return item.content_html


class CategoryFeed(Feed):
    link = ''

    def title(self, item):
        return 'Latest posts for category: ' + item.name

    def get_object(self, request, slug):
        return models.Category.objects.get(slug=slug)

    def items(self, item):
        return models.Article.objects.published().filter(category=item)

    def item_description(self, item):
        if len(item.content) > FEED_DESCRIPTION_MAX:
            return item.content_html[:FEED_DESCRIPTION_MAX] + '...'
        else:
            return item.content_html


class TagFeed(Feed):
    link = ''

    def title(self, item):
        return item.name

    def get_object(self, request, slug):
        return models.Tag.objects.get(slug=slug)

    def items(self, item):
        return models.Article.objects.published().filter(tags=item)

    def item_description(self, item):
        if len(item.content) > FEED_DESCRIPTION_MAX:
            return item.content_html[:FEED_DESCRIPTION_MAX] + '...'
        else:
            return item.content_html
