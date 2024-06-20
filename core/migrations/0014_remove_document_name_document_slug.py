# Generated by Django 5.0.6 on 2024-06-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=254, verbose_name='Name'),
        ),
    ]
