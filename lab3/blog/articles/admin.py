# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Article

# настройки админки
class ArticleAdmin(admin.ModelAdmin):
    # какие поля показывать в списке
    list_display = ('title', 'author', 'get_excerpt', 'created_date')

# регистрируем модель
admin.site.register(Article, ArticleAdmin)