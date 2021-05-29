from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView, 
                                  UpdateView,
                                  DeleteView,)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post

def home(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "blog/home.html",context)

def about(request):
    return render(request, "blog/about.html", {'title':'About'})

class BlogListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/home.html"
    ordering = ['-date']
    paginate_by = 5

class UserBlogListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/user_posts.html"
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class BlogDetailView(DetailView):
    model = Post

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author