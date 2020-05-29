from django.urls import path
from . import views1
from .forms import PostForm

urlpatterns=[
    path('', views1.postlists, name='post_list'),
    path('post/<int:pk>/', views1.post_detail, name='post_detail'),
    path('post/new/', views1.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views1.post_edit, name='post_edit'),
    path(r'^drafts/$', views1.post_draft_list, name='post_draft_list'),
    path(r'^post/(?P<pk>\d+)/publish/$', views1.post_publish, name='post_publish'),
    path(r'^post/(?P<pk>\d+)/remove/$', views1.post_remove, name='post_remove'),
    path(r'^post/(?P<pk>\d+)/comment/$', views1.add_comment_to_post, name='add_comment_to_post'),
    path(r'^comment/(?P<pk>\d+)/approve/$', views1.comment_approve, name='comment_approve'),
    path(r'^comment/(?P<pk>\d+)/remove/$', views1.comment_remove, name='comment_remove'),
    # path(r'contact/', views.contact, name='contacts'),
    # path(r'about/', views.about, name='about')

]