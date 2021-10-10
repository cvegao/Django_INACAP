from django.urls import path

from books_authors_app import views

urlpatterns = [
    path('', views.books, name='books'),
    path('books/add_book', views.add_book, name='add_book'),
    path('books/show_book', views.show_book, name='show_book'),
    path('authors/', views.authors, name='authors'),
    path('authors/add_author', views.add_author, name='add_author'),
    path('authors/show_author', views.show_author, name='show_author'),
    path('books/authors', views.assign_author, name='assign_author'),
    path('authors/books', views.assign_book, name='assign_book'),
]
