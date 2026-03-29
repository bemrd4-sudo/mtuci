# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Article

# главная страница со всеми статьями
def archive(req):
    # берем все статьи из базы
    posts = Article.objects.all()
    return render(req, 'archive.html', {"posts": posts})