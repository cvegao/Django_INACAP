from django.db import models


class Dojo(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=225)


class Ninja(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
