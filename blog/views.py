from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage
from django.shortcuts import Http404
from django.views import generic

from .models import Blog


def index(request, page=1):
    try:
        p = Paginator(Blog.objects.order_by('-id'), 3)
        blogs = p.page(page)
    except InvalidPage:
        raise Http404
    return render(request, 'blog/blog.html', {'blog': blogs})


class Post(generic.DetailView):
    model = Blog
    context_object_name = 'post'
    template_name = 'blog/blog-inside.html'
