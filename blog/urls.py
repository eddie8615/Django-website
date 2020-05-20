from django.urls import path
from . import views1
from .forms import PostForm

urlpatterns=[
    path('', views1.postlists),
    path('post/<int:pk>/', views1.post_detail, name='post_detail'),
    path('post/new/', views1.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views1.post_edit, name='post_edit'),
    # path(r'contact/', views.contact, name='contacts'),
    # path(r'about/', views.about, name='about')

]