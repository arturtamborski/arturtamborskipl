from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.urls import reverse
from . import models


class PostRssFeed(Feed):
    description = ''
    link = '/'
    title = 'Latest posts'

    def items(self, obj):
        return models.Article.objects.published()

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse('article', args=[item.slug])

class PostAtomFeed(PostRssFeed):
    feed_type = Atom1Feed
    subtitle = PostRssFeed.description


class CategoryRssFeed(Feed):
    description = ''

    def get_object(self, request, slug):
        return models.Category.objects.get(slug=slug)

    def title(self, obj):
        return obj.name

    def link(self, obj):
        return obj.get_absolute_url()

    def items(self, obj):
        return models.Article.objects.published().filter(category=obj)

class CategoryAtomFeed(CategoryRssFeed):
    feed_type = Atom1Feed
    subtitle = CategoryRssFeed.description


class TagRssFeed(Feed):
    description = ''

    def get_object(self, request, slug):
        return models.Tag.objects.get(slug=slug)

    def title(self, obj):
        return obj.name

    def link(self, obj):
        return obj.get_absolute_url()

    def items(self, obj):
        return models.Article.objects.published().filter(tags=obj)

class TagAtomFeed(TagRssFeed):
    feed_type = Atom1Feed
    subtitle = TagRssFeed.description
