# Generated by Django 3.2.5 on 2021-08-31 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_orm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wizard',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
