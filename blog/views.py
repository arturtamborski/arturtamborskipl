from django.utils import timezone
from django.shortcuts import render

from . import models as blog

def article(request, slug=None):
    objects = blog.Article.objects.published()
    if slug is not None:
        objects = objects.filter(slug=slug)

    return render(request, 'blog/article.html', {
        'isroot': slug is None,
        'articles': objects,
        })



def category(request, slug=None):
    objects = blog.Category.objects.all()
    if slug is not None:
        objects = objects.filter(slug=slug)

    return render(request, 'blog/category.html', {
        'isroot': slug is None,
        'categories': objects,
        })



def tag(request, slug=None):
    objects = blog.Tag.objects.all()
    if slug is not None:
        objects = objects.filter(slug=slug)

    return render(request, 'blog/tag.html', {
        'isroot': slug is None,
        'tags': objects,
        })



def search(request):
    q = request.GET.get('q', '')
    objects = blog.Article.objects.search(q)

    return render(request, 'blog/search.html', {
            'objects': objects,
        })
