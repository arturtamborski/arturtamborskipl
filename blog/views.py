from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import models as blog

PAGE_MAX = 5


def get_objects(request, objects, slug=None):
    if slug is not None:
        objects = objects.filter(slug=slug)

    page = request.GET.get('p', 1)
    paginator = Paginator(objects, PAGE_MAX)

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects

def article(request, slug=None):
    articles = get_objects(
        request, blog.Article.objects.published(), slug)

    return render(request, 'blog/article.html', {
        'isroot': slug is None,
        'articles': articles,
        })



def category(request, slug=None):
    categories = get_objects(
            request, blog.Category.objects.all(), slug)

    return render(request, 'blog/category.html', {
        'isroot': slug is None,
        'categories': categories,
        })



def tag(request, slug=None):
    tags = get_objects(
            request, blog.Tag.objects.all(), slug)

    return render(request, 'blog/tag.html', {
        'isroot': slug is None,
        'tags': tags,
        })



def search(request):
    q = request.GET.get('q', '')
    objects = get_objects(
            request, blog.Article.objects.search(q), slug)

    return render(request, 'blog/search.html', {
            'objects': objects,
        })



def home(request):
    return article(request)

def about(request):
    return article(request, slug='about')
