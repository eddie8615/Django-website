from django.urls import path
from . import views

urlpatterns=[
    path('', views.bloghome),
    # path(r'contact/', views.contact, name='contacts'),
    # path(r'about/', views.about, name='about')

]