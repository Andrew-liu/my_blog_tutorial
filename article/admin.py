# -*- coding: utf-8 -*-

from django.contrib import admin
from article.models import Article
from article.models import Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_time')
    search_fields = ('title', 'category', 'tag', 'content')
    list_filter = ("date_time",)
    raw_id_fields = ('tag', )    
    date_hierarchy = 'date_time'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
