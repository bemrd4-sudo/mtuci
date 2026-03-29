# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
    if req.user.is_anonymous():
        raise Http404
    
    if req.method == "POST":
        title = req.POST.get("title", "")
        text = req.POST.get("text", "")
        
        if not title or not text:
            return render(req, 'create_post.html', {
                'error': u"заполни все поля",
                'title': title,
                'text': text
            })
        
        try:
            Article.objects.get(title=title)
            return render(req, 'create_post.html', {
                'error': u"такое название уже есть",
                'title': title,
                'text': text
            })
        except Article.DoesNotExist:
            article = Article.objects.create(
                title=title,
                text=text,
                author=req.user
            )
            return redirect('get_article', article_id=article.id)
    else:
        return render(req, 'create_post.html', {})

# логин
def login_view(req):
    if req.method == "POST":
        username = req.POST.get("username", "")
        password = req.POST.get("password", "")
        
        if not username or not password:
            return render(req, 'login.html', {
                'error': u"заполни все поля"
            })
        
        user = authenticate(username=username, password=password)
        if user:
            login(req, user)
            return redirect('archive')
        else:
            return render(req, 'login.html', {
                'error': u"неправильный логин или пароль"
            })
    else:
        return render(req, 'login.html', {})

# логаут
def logout_view(req):
    logout(req)
    return redirect('archive')

# регистрация
def register_view(req):
    if req.method == "POST":
        username = req.POST.get("username", "")
        email = req.POST.get("email", "")
        password = req.POST.get("password", "")
        pass2 = req.POST.get("password_confirm", "")
        
        if not username or not email or not password or not pass2:
            return render(req, 'register.html', {
                'error': u"заполни все поля"
            })
        
        if password != pass2:
            return render(req, 'register.html', {
                'error': u"пароли не совпадают"
            })
        
        try:
            User.objects.get(username=username)
            return render(req, 'register.html', {
                'error': u"такой пользователь уже есть"
            })
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            user.save()
            # сразу логиним после регистрации
            user = authenticate(username=username, password=password)
            login(req, user)
            return redirect('archive')
    else:
        return render(req, 'register.html', {})