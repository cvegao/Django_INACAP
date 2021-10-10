from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.show_clients, name='show_clients'),
]
