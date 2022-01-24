from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'theme/index.html', {'blogs': blogs})
def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'theme/blog.html', {'blog': blog})

