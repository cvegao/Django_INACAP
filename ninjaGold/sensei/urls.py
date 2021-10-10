from django.urls import path

from sensei import views

urlpatterns = [
    path('', views.set_conditions, name="set_conditions"),
]