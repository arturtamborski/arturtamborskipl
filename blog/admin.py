from django.contrib import admin

from .models import Tag, Category, Article

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ordering = ('-date',)
    list_filter = ('date',)
    list_display = ('id', 'title', 'date', 'category',)
    search_fields = ('id', 'title', 'date', 'category',)
    date_hierarchy = 'date'
    filter_horizontal = ('tags',)
