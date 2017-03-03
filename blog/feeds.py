from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.urls import reverse
from . import models


class ArticleFeed(Feed):
    title = 'Latest posts'

    def get_object(self, request, slug):
        return models.Articles.objects.published().get(slug=slug)

    def title(self, item):
        return item.title

    def description(self, item):
        return (item.content[:80] + '...') if len(item.content) > 80 else item.content

    def link(self, item):
        return reverse('article', args=[item.slug])

    def items(self, obj):
        return models.Article.objects.published()


class CategoryFeed(Feed):
    description = ''

    def get_object(self, request, slug):
        return models.Category.objects.get(slug=slug)

    def title(self, item):
        return item.name

    def link(self, item):
        return item.get_absolute_url()

    def items(self, item):
        return models.Article.objects.published().filter(category=item)


class TagFeed(Feed):
    description = ''

    def get_object(self, request, slug):
        return models.Tag.objects.get(slug=slug)

    def title(self, item):
        return item.name

    def link(self, item):
        return item.get_absolute_url()

    def items(self, item):
        return models.Article.objects.published().filter(tags=item)
