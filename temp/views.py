from django.shortcuts import render
from .models import Blog
# Create your views here.


def home(request):
    template_name = 'temp/index.html'
    blog_list = Blog.objects.all()
    context_object = {
        'blog_list': blog_list,
    }

    return render(request, template_name, context_object)


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    template_name = 'temp/blog-detail.html'
    context_object = {
        'blog': blog,
    }
    return render(request, template_name, context_object)


