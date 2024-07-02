# myapp/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'subtitle', 'description', 'image']
    template_name = 'blog_form.html'  # Make sure this matches your template name
    success_url = reverse_lazy('blog_list')  # Redirect to 'blog_list' URL after successful creation
class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ['title', 'subtitle', 'description', 'image']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')
