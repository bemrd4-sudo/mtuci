# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from models import Article

# все статьи
def archive(req):
    posts = Article.objects.all()
    return render(req, 'archive.html', {"posts": posts})

# одна статья
def get_article(req, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(req, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

# новая статья
def create_post(req):
    # проверка что пользователь залогинен
    if req.user.is_anonymous():
        raise Http404
    
    if req.method == "POST":
        # данные из формы
        title = req.POST.get("title", "")
        text = req.POST.get("text", "")
        
        # проверка что поля не пустые
        if not title or not text:
            return render(req, 'create_post.html', {
                'error': u"заполни все поля!",
                'title': title,
                'text': text
            })
        
        # проверка на уникальность названия
        try:
            Article.objects.get(title=title)
            return render(req, 'create_post.html', {
                'error': u"такое название уже есть",
                'title': title,
                'text': text
            })
        except Article.DoesNotExist:
            # все ок, создаем статью
            article = Article.objects.create(
                title=title,
                text=text,
                author=req.user
            )
            return redirect('get_article', article_id=article.id)
    else:
        # просто показываем форму
        return render(req, 'create_post.html', {})