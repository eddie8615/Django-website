from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

#def contact(request):
#   return render(request, 'blog/contact.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def postlists(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/index.html', {'posts':posts})