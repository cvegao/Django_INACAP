from django.urls import path

from shows_crud import views

urlpatterns = [
    path('', views.read_all, name='read_all'),  # GET
    path('shows/', views.read_all, name='read_all'),  # GET
    path('shows/new/', views.new_show, name="new_show"),  # GET
    path('shows/create/', views.create_show, name="create_show"),  # POST
    path('shows/<id>/edit/', views.edit_show, name="edit_show"),  # GET
    path('shows/update/', views.update_show, name="update_show"),  # POST
    path('shows/<id>/', views.read_one, name="read_one"),  # GET
    path('shows/<id>/destroy/', views.destroy, name="destroy"),  # GET
]