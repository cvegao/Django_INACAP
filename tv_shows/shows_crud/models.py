from django.db import models
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class ShowManager(models.Manager):
    def validations(self, data):
        errors = {}
        if len(data['title']) == 0:
            errors['title'] = "Title field cannot be empty"
        elif len(data['network']) == 0:
            errors['network'] = "Network field cannot be empty"
        elif len(data['release_date']) == 0:
            errors['release_date'] = "Release date field cannot be empty"
        elif len(data['description']) == 0:
            errors['description'] = "Description field cannot be empty"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=150)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    objects = ShowManager()

    class Meta:
        db_table = 'shows'
