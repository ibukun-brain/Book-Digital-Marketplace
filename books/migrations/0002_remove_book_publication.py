# Generated by Django 3.2.7 on 2022-12-27 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publication',
        ),
    ]