# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# модель статьи
class Article(models.Model):
    title = models.CharField(max_length=200)  # заголовок
    author = models.ForeignKey(User)  # автор (связь с юзерами)
    text = models.TextField()  # текст статьи
    created_date = models.DateField(auto_now_add=True)  # дата создания
    
    def __unicode__(self):
        # чтоб красиво выводилось
        return u"%s: %s" % (self.author.username, self.title)
    
    def get_excerpt(self):
        # первые 140 символов текста
        if len(self.text) > 140:
            return u"%s..." % self.text[:140]
        return self.text