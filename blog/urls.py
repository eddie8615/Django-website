from django.urls import path
from . import views

urlpatterns=[
    path('', views.postlists),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
    # path(r'contact/', views.contact, name='contacts'),
    # path(r'about/', views.about, name='about')

]