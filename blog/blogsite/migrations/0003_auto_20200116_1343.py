# Generated by Django 3.0.2 on 2020-01-16 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0002_planos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Planos',
            new_name='Plano',
        ),
    ]