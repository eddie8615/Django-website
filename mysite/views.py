from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def about(request):
    return render(request, 'about.html')

def homepage(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'index.html', {})