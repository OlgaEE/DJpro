from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

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
        'title': 'Main Page',
        'cat_selected': 0,
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


def show_post(request, post_slug):
    post = get_object_or_404(Learnings, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': 1,
    }
    return render(request, 'learnings/post.html', context=context)


def show_category(request, cat_id):
    posts = Learnings.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Swoing Category',
        'cat_selected': cat_id,
    }
    return render(request, 'learnings/index.html', context=context)


