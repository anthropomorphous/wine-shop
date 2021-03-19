from django.urls import path, include
from . import views

#
# /products/1/detail
# /products/new

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('<int:id>/', views.detail, name='detail'),
    path('new', views.new),
]
