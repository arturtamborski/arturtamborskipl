from django.http import Http404, HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_list_or_404
from . import models as blog

def article(request, slug=None):
    prev = None
    articles = blog.Article.objects.published()
    if slug is not None:
        articles = articles.filter(slug=slug)

    return render(request, 'blog/article.html', {
        'isroot': slug is None,
        'articles': articles,
        })



def category(request, slug=None):
    categories = blog.Category.objects.all()
    if slug is not None:
        categories = categories.filter(slug=slug)

    return render(request, 'blog/category.html', {
        'isroot': slug is None,
        'categories': categories,
        })



def tag(request, slug=None):
    tags = blog.Tag.objects.all()
    if slug is not None:
        tags = tags.filter(slug=slug)

    return render(request, 'blog/tag.html', {
        'isroot': slug is None,
        'tags': tags,
        })


def search(request):
    if 'q' in request.GET:
        results = blog.Article.objects.search(request.GET['q'])
        
    return render(request, 'blog/search.html', {
        'results': results
        })



def meta(request):
    values = sorted(request.META.items())
    response = []
    for key, value in values:
        response.append('<tr><td>{}</td><td>{}</td></tr>'.format(key, value))
    return HttpResponse('<table>{}</table>'.format('\n'.join(response)))



def home(request):
    return article(request)
