# Generated by Django 3.1.4 on 2021-01-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cat',
        ),
        migrations.AddField(
            model_name='product',
            name='wine_type',
            field=models.CharField(choices=[('WHITE', 'White'), ('RED', 'Red'), ('ROSE', 'Rose')], default='WHITE', max_length=100, null=True),
        ),
    ]
