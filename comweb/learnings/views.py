from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': "About Sait", 'url_name': 'about'},
        {'title': "Add Article", 'url_name': 'add_page'},
        {'title': "FedBack", 'url_name': 'contact'},
        {'title': "LogIn", 'url_name': 'login'}
]

class LearningsHome(ListView):      #for main page showing
    model = Learnings
    template_name = 'learnings/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main Page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Learnings.objects.filter(is_published=True)



#def index(request):
#    posts = Learnings.objects.all()

#    context = {
 #       'posts': posts,
#      'menu': menu,
#       'title': 'Main Page',
#       'cat_selected': 0,
#   }
#   return render(request, 'learnings/index.html', context=context)


def about(request):
    return render(request, 'learnings/about.html', {'menu': menu, 'title': 'About This Site'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'learnings/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Article Adding'
        context['menu'] = menu
        return context


#def addpage(request):
#   if request.method == 'POST':
#       form = AddPostForm(request.POST, request.FILES)
#       if form.is_valid():
#           #print(form.cleaned_data)
#           form.save()
#           return redirect('home')
#   else:
#       form = AddPostForm()
#   return render(request, 'learnings/addpage.html', {'form': form, 'menu': menu, 'title': 'Article Adding'})


def contact(request):
    return HttpResponse("FedBack")


def login(request):
    return HttpResponse("LogIn")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')


#def show_post(request, post_slug):
#   post = get_object_or_404(Learnings, slug=post_slug)

#   context = {
#       'post': post,
#       'menu': menu,
#       'title': post.title,
#       'cat_selected': 1,
#   }
#   return render(request, 'learnings/post.html', context=context)
class ShowPost(DetailView):
    model = Learnings
    template_name = 'learnings/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

class LearningsCategory(ListView):
    model = Learnings
    template_name = 'learnings/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Learnings.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context


#def show_category(request, cat_id):
#    posts = Learnings.objects.filter(cat_id=cat_id)

#    if len(posts) == 0:
#       raise Http404

#   context = {
#       'posts': posts,
#       'menu': menu,
#       'title': 'Showing Category',
#       'cat_selected': cat_id,
#   }
#   return render(request, 'learnings/index.html', context=context)
