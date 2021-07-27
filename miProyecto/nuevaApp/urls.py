from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # http://localhost:8000/
    path('manzanas', views.mostrar_todas, name='mostrar_manzanas'),  # http://localhost:8000/manzanas
    path('manzanas/<int:id>', views.mostrar_por_id, name='mostrar_por_id'),  # http://localhost:8000/manzanas/2
    path('manzanas/<string:origen>/variedades', views.mostrar_variedades_por_origen, name='mostrar_variedades_por_origen'),  # http://localhost:8000/manzanas/chile/variedades
]