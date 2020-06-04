from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):
  template_name = 'blog/index.html'
  try:
    post_list = Post.objects.all()
  except:
    post_list = None 
  context_object = {
    'post_list': post_list,
  }

  return render(request, template_name, context_object)


def blog_detail(request, pk):
  template_name = 'blog/blog-detail.html'
  try:
    post = Post.objects.get(pk=pk)
  except:
    post = None 
  context_object = {
    'post': post,
  }
  return render(request, template_name, context_object)


