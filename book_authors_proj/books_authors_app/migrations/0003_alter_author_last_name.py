# Generated by Django 3.2.7 on 2021-09-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20210925_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
