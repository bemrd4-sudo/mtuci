# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous():
        if request.method == "POST":
            form = {
                'text': request.POST.get("text", ""),
                'title': request.POST.get("title", "")
            }
            
            if form["text"] and form["title"]:
                try:
                    Article.objects.get(title=form["title"])
                    form['errors'] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                except Article.DoesNotExist:
                    article = Article.objects.create(
                        text=form["text"],
                        title=form["title"],
                        author=request.user
                    )
                    return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404

# АВТОРИЗАЦИЯ
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                return render(request, 'login.html', {
                    'errors': u"Неверный логин или пароль"
                })
        else:
            return render(request, 'login.html', {
                'errors': u"Заполните все поля"
            })
    else:
        return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect('archive')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        password_confirm = request.POST.get("password_confirm", "")
        
        if username and email and password and password_confirm:
            if password != password_confirm:
                return render(request, 'register.html', {
                    'errors': u"Пароли не совпадают"
                })
            
            try:
                User.objects.get(username=username)
                return render(request, 'register.html', {
                    'errors': u"Пользователь с таким именем уже существует"
                })
            except User.DoesNotExist:
                user = User.objects.create_user(username, email, password)
                user.save()
                
                # Автоматически авторизуем после регистрации
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('archive')
        else:
            return render(request, 'register.html', {
                'errors': u"Заполните все поля"
            })
    else:
        return render(request, 'register.html', {})