# Generated by Django 3.1.4 on 2021-01-17 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0005_auto_20210116_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='image',
        ),
    ]