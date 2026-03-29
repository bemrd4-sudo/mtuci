# -*- coding: utf-8 -*-
from django.shortcuts import render

# главная страница
def home(req):
    return render(req, 'index.html', {})

# страница с картинкой и стилями
def static_handler(req):
    return render(req, 'static_handler.html', {})