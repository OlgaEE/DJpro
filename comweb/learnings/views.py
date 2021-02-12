from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "About Sait", 'url_name': 'about'},
        {'title': "Add Article", 'url_name': 'add_page'},
        {'title': "FedBack", 'url_name': 'contact'},
        {'title': "LogIn", 'url_name': 'login'}
]

def index(request):
    posts = Learnings.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main Page'
    }
    return render(request, 'learnings/index.html', context=context)


def about(request):
    return render(request, 'learnings/about.html', {'menu': menu, 'title': 'About This Site'})


def addpage(request):
    return HttpResponse("Add Article")


def contact(request):
    return HttpResponse("FedBack")


def login(request):
    return HttpResponse("LogIn")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')


def show_post(request, post_id):
    return HttpResponse(f"Show article with id = {post_id}")

