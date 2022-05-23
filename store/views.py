from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Добро пожаловать в наш магазин</h1>")

def contact(request):
    return HttpResponse('<h2>Наши контакты</h2>')

def about_us(request):
    return HttpResponse('<h3>О нас</h3>')