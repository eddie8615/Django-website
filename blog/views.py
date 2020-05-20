from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

#def contact(request):
#   return render(request, 'blog/contact.html')

#def about(request):
#    return render(request, 'blog/about.html')

def bloghome(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/index.html', {'posts':posts})