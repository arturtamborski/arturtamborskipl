from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from blog import views as blog

class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(blog.category, args=[self.slug])



class Tag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self, self.name)
        super(Tag, self).save(*args, **kwargs)



class Article(models.Model):
    title    = models.CharField(max_length=256)
    slug     = models.SlugField(unique=True, editable=False)
    date     = models.DateTimeField(default=timezone.now)
    tags     = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    prologue = models.TextField()
    content  = models.TextField()
    epilogue = models.TextField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'{}'.format(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(blog.article, args=[self.slug])
