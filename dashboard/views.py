from django.shortcuts import render

# Create your views here.

# Components: blog previews, cv
def list_apps(request):
    return render(request, 'index.html', {})