from django.http import Http404, HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_list_or_404
from . import models as blog

def article(request, slug=None):
    articles = blog.Article.objects.published().filter(slug=slug)
    if slug is None:
        articles = blog.Article.objects.published()

    return render(request, 'blog/article.html', {
        'isroot': slug is None,
        'articles': articles,
        })



def category(request, slug=None):
    categories = blog.Category.objects.filter(slug=slug)
    if slug is None:
        categories = blog.Category.objects.all()

    return render(request, 'blog/category.html', {
        'isroot': slug is None,
        'categories': categories,
        })



def tag(request, slug=None):
    tags = blog.Tag.objects.all().filter(slug=slug)
    if slug is None:
        tags = blog.Tag.objects.all()

    return render(request, 'blog/tag.html', {
        'isroot': slug is None,
        'tags': tags,
        })



def search(request):
    if 'q' in request.GET and len(request.GET['q']):
        q = request.GET['q']
        articles    = blog.Article.objects.search(q)
#        categories  = blog.Category.objects.search(q)
#        tags        = blog.Tag.objects.search(q)

    return render(request, 'blog/search.html', {
            'articles': articles,
#            'categories': categories,
#            'tags': tags,
        })



def home(request):
    articles = blog.Article.objects.published()[:5]

    return render(request, 'blog/article.html', {
        'isroot': True,
        'articles': articles,
        })



def about(request):
    # FIXME: This is just temporary solution
    article(request, slug='about')
