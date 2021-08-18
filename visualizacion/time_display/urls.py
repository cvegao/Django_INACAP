from django.urls import path

from time_display import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api', views.api_index, name='api'),
]