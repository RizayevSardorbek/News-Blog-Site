from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'full.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'add.html'
    fields = ['title', 'body', 'author']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


