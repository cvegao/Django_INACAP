from django.urls import path

from random_word import views

urlpatterns = [
    path('', views.show_word, name='word_generator'),
    path('reset', views.reset_attempts, name='reset_attempts'),
]
