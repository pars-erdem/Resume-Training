# Generated by Django 5.0.6 on 2024-06-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_imagesettings_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesettings',
            name='description',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Description'),
        ),
    ]
