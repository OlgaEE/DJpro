from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["About This Site", "Add Article", "Fedback", "LogIn"]

def index(request):
    posts = Learnings.objects.all()
    return render(request, 'learnings/index.html', {'posts': posts, 'menu': menu, 'title': 'Main Page'})


def about(request):
    return render(request, 'learnings/about.html', {'menu': menu, 'title': 'About This Site'})


def categories(request, catid):
    return HttpResponse(f"<h1>Learn by Categories</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Archive by Years</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')

