from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="blogs_index"),
    path('new', views.new, name="new_blog"),
    path('create', views.create, name="create_blog"),
    path('<int:number>', views.show, name="show_blog_by_id"),
    path('<int:number>/edit', views.edit, name="edit_blog_by_id"),
    path('<int:number>/delete', views.destroy, name="delete_blog_by_id"),
    path('json', views.show_as_json, name="show_blogs_as_json"),
    ]
