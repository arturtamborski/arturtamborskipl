from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from . import models as blog

def home(request):
    NUM_LAST_ARTICLES = 3

    try:
        # find three latest articles and sort them from latest one 
        articles = blog.Article.objects.defer('content').filter(date__lte=timezone.now()).order_by('-date')[:NUM_LAST_ARTICLES]
    except ObjectDoesNotExist:
        raise Http404('Article does not exist!')

    return render(request, 'blog/home.html', { 'articles': articles })
