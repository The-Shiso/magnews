# Generated by Django 2.2.5 on 2019-10-08 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0002_cat_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='count',
        ),
    ]