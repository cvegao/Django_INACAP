from django.db import models
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class BookManager(models.Manager):
    def validations(self, data):
        errors = {}
        if len(data['title']) == 0:
            errors['title'] = "Title is required"
        elif len(data['title']) > 255:
            errors['title'] = "Title cannot be longer than 255 characters"
        return errors


class AuthorManager(models.Manager):
    def validations(self, data):
        errors = {}
        if len(data['first_name']) == 0:
            errors['first_name'] = "First name is required"
        elif len(data['first_name']) > 45:
            errors['first_name'] = "First name cannot be longer than 45 characters"
        if len(data['first_name']) > 45:
            errors['last_name'] = "Last name cannot be longer than 45 characters"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)  # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = AutoDateTimeField(default=timezone.now)  # updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    class Meta:
        db_table = 'books'


class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    books = models.ManyToManyField(Book, related_name='authors', db_table='books_authors')
    notes = models.TextField(null=True)
    objects = AuthorManager()

    class Meta:
        db_table = 'authors'
