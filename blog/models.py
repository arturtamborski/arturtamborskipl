from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

from .markup import markup

class CategoryQuerySet(models.QuerySet):
    def search(self, term):
        return self.filter(name__icontains=term)



class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True, editable=False)

    objects = CategoryQuerySet().as_manager()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])



class TagQuerySet(models.QuerySet):
    def search(self, term):
        return self.filter(name__icontains=term)



class Tag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, editable=False)

    objects = TagQuerySet().as_manager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self, self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tag', args=[self.slug])


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(date__lte=timezone.now())

    def search(self, term):
        return self.published().filter(title__icontains=term)

    def prev(self, date):
        """ Return previous posts relative to `date` """
        return self.published().filter(date__lt=date)

    def next(self, date):
        """ Return next posts relative to `date` """
        return self.published().filter(date__gt=date)



class Article(models.Model):
    title    = models.CharField(max_length=256)
    slug     = models.SlugField(unique=True, editable=False)
    date     = models.DateTimeField(default=timezone.now)
    tags     = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    content  = models.TextField()
    content_html = models.TextField(editable=False, blank=True)

    objects = ArticleQuerySet().as_manager()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.content_html = markup(self.content)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article', args=[self.slug])

    def is_published(self):
        return self.date <= timezone.now()

    def prev(self):
        """
            return previous article relative to `self`.
            Im not sure about this method. Is there a better one?
            Maybe Manager should take care of this...
        """
        try:
            return Article.objects.prev(self.date).first()
        except IndexError as e:
            return 0

    def next(self):
        try:
            return Article.objects.next(self.date).last()
        except IndexError as e:
            return 0
