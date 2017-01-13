from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'{}'.format(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'{}'.format(self.name)

class Article(models.Model):
    title    = models.CharField(max_length=256)
    slug     = models.SlugField(editable=False)
    date     = models.DateField()
    tags     = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    body     = models.TextField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'{}'.format(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
