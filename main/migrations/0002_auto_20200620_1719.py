# Generated by Django 3.0.7 on 2020-06-20 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='authors',
        ),
    ]
