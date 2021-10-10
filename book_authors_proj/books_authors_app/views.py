from django.shortcuts import render, redirect

from books_authors_app.models import Book, Author


def books(request):
    books_list = Book.objects.all()
    context = {'books': books_list}
    return render(request, 'books_authors_app/books.html', context)


def add_book(request):
    errores = Book.objects.validations(request.POST)
    if not errores:
        title = request.POST['title']
        description = request.POST['description']
        Book.objects.create(title=title, desc=description)
    return redirect('books')


def authors(request):
    authors_list = Author.objects.all()
    context = {'authors': authors_list}
    return render(request, 'books_authors_app/authors.html', context)


def add_author(request):
    errores = Author.objects.validations(request.POST)
    if not errores:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('authors')


def show_book(request):
    id = request.POST['id']
    book = Book.objects.get(id=id)
    authors_list = Author.objects.exclude(books=book)
    context = {'book': book, 'authors_list': authors_list}
    return render(request, 'books_authors_app/show_book.html', context)


def assign_author(request):
    book_id = request.POST['book_id']
    book = Book.objects.get(id=book_id)
    author_id = request.POST['author_id']
    author = Author.objects.get(id=author_id)
    is_author_in_book = book.authors.filter(id=author_id)
    if not is_author_in_book:
        book.authors.add(author)
        book.save()
    authors_list = Author.objects.exclude(books=book)
    context = {'book': book, 'authors_list': authors_list}
    return render(request, 'books_authors_app/show_book.html', context)


def show_author(request):
    id = request.POST['id']
    author = Author.objects.get(id=id)
    books_list = Book.objects.exclude(authors=author)
    context = {'author': author, 'books_list': books_list}
    return render(request, 'books_authors_app/show_author.html', context)


def assign_book(request):
    book_id = request.POST['book_id']
    book = Book.objects.get(id=book_id)
    author_id = request.POST['author_id']
    author = Author.objects.get(id=author_id)
    is_book_in_author = author.books.filter(id=book_id)
    if not is_book_in_author:
        author.books.add(book)
        author.save()
    books_list = Book.objects.exclude(authors=author)
    context = {'author': author, 'books_list': books_list}
    return render(request, 'books_authors_app/show_author.html', context)