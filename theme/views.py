from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    portfolios = Portfolio.objects.all()
    return render(request, 'theme/index.html', {'blogs': blogs, 'portfolios': portfolios})
def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'theme/blog.html', {'blog': blog})

def category(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, 'theme/category.html', {'category': category})