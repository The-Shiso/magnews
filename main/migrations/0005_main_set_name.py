# Generated by Django 2.2.5 on 2019-09-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190930_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.TextField(default='-'),
        ),
    ]
