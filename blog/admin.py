from django.contrib import admin
from . import models as blog 

class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_filter = ('id', 'name',)
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)

class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_filter = ('id', 'name',)
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)

class ArticleAdmin(admin.ModelAdmin):
    ordering = ('-date',)
    list_filter = ('id', 'date',)
    list_display = ('id', 'title', 'date', 'category',)
    search_fields = ('id', 'title', 'date', 'category',)
    date_hierarchy = 'date'
    filter_horizontal = ('tags',) # for ease of use

admin.site.register(blog.Article, ArticleAdmin)
admin.site.register(blog.Category, CategoryAdmin)
admin.site.register(blog.Tag, TagAdmin)
