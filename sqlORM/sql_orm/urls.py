from django.urls import path, include

from sql_orm import views

urlpatterns = [
    path('', views.index, name='hp_index'),
    path('create/', views.create_wizard, name='create_wizard'),
    path('edit-form/', views.edit_wizard_form, name='edit_wizard_form'),
    path('edit/', views.edit_wizard, name='edit_wizard'),
    path('delete/', views.delete_wizard, name='delete_wizard'),
    path('error/', views.error, name='error'),
]
