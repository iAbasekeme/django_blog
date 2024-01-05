from django.shortcuts import render
from datetime import datetime
from blog.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name = 'post'   
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post    
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title", "content"]
    
    # Direct the created view to the request user
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response   
    
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About page'})
