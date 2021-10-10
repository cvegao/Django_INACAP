from django.db import models


class WizardManager(models.Manager):
    def validations(self, data):
        errors = {}

        for attr in Wizard.__attrs__(self):
            if len(data[attr]) == 0:
                errors[attr] = f"{str.capitalize(attr)} can not be empty"

        return errors


class Wizard(models.Model):
    class Houses(models.TextChoices):
        GRYFFINDOR = "Gryffindor"
        SLYTHERIN = "Slytherin"
        RAVENCLAW = "Ravenclaw"
        HUFFLEPUFF = "Hufflepuff"

    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45, choices=Houses.choices)
    pet = models.CharField(max_length=45)
    year = models.IntegerField(default=0)
    objects = WizardManager()

    def __attrs__(self):
        return ["name", "house", "pet", "year"]

    class Meta:
        db_table = 'wizards'
