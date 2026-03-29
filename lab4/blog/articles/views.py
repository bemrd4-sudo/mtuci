# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from models import Article

# все статьи
def archive(req):
    posts = Article.objects.all()
    return render(req, 'archive.html', {"posts": posts})

# одна статья по id
def get_article(req, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(req, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404  # нет такой статьи