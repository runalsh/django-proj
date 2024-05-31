from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import News


# Create your views here.
def index(request):
    news=News.objects.all()
    return render(request,'news/index.html',{'news':news, 'title':'список новостей' })

