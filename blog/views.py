from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from . import models as blog



def home(request):
    NUM_LAST_ARTICLES = 5

    articles = blog.Article.objects.filter(date__lte=timezone.now()).order_by('-date')[:NUM_LAST_ARTICLES]

    return render(request, 'blog/article.html', {'isroot': True, 'articles': articles})



def article(request, slug=None):
    if slug is None:
        articles = get_list_or_404(blog.Article)
    else:
        articles = get_list_or_404(blog.Article, slug=slug)

    return render(request, 'blog/article.html', {
        'isroot': bool(slug is None),
        'articles': articles
        })




def category(request, slug=None):
    if slug is None:
        categories = get_list_or_404(blog.Category)
    else:
        categories = get_list_or_404(blog.Category, slug=slug)

    return render(request, 'blog/category.html', {
        'isroot': bool(slug is None),
        'categories': categories,
        })


def meta(request):
    values = sorted(request.META.items())
    html = []
    for key, value in values:
        html.append('<tr><td>{}</td><td>{}</td></tr>'.format(key, value))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
