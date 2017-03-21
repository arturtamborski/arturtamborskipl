from django.utils import timezone
from django.shortcuts import render
from django.views import generic
from . import models


class ArticleList(generic.ListView):
    queryset            = models.Article.objects.published()
    template_name       = 'blog/articles.html'
    context_object_name = 'articles'

class ArticleDetail(generic.DetailView):
    model               = models.Article
    template_name       = 'blog/article.html'
    context_object_name = 'article'

class CategoryList(generic.ListView):
    queryset            = models.Category.objects.all()
    template_name       = 'blog/categories.html'
    context_object_name = 'categories'

class CategoryDetail(generic.DetailView):
    model               = models.Category
    template_name       = 'blog/category.html'
    context_object_name = 'category'

class TagList(generic.ListView):
    queryset            = models.Tag.objects.all()
    template_name       = 'blog/tags.html'
    context_object_name = 'tags'

class TagDetail(generic.DetailView):
    model               = models.Tag
    template_name       = 'blog/tag.html'
    context_object_name = 'tag'

class SearchList(generic.ListView):
    model               = models.Article
    template_name       = 'blog/search.html'
    context_object_name = 'objects'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        objects = models.Article.objects.search(q)
        return objects
