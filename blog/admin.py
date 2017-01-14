from django.contrib import admin
from . import models as blog 

class ArticleAdmin(admin.ModelAdmin):
    ordering = ('-date',)
    list_filter = ('id', 'date',)
    list_display = ('id', 'title', 'date', 'category',)
    search_fields = ('id', 'title', 'date', 'category',)
    date_hierarchy = 'date'
    filter_horizontal = ('tags',) # for ease of use

admin.site.register(blog.Article, ArticleAdmin)
admin.site.register(blog.Category)
admin.site.register(blog.Tag)
