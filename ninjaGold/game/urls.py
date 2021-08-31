from django.urls import path

from game import views

urlpatterns = [
    path('', views.index, name="index"),
    path('process_money', views.process_money, name="process_money"),
    path('restart', views.restart_session, name="restart_session"),
]