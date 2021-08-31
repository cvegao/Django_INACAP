from django.urls import path

from ninja_bonus import views

urlpatterns = [
    path('', views.index, name="index_bonus"),
    path('place/<place>/', views.process_money, name="process_money_bonus"),
    path('restart/', views.restart_session, name="restart_session_bonus"),
]
