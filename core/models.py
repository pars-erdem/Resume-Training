from django.db import models

# Create your models here.
class GeneralSettings(models.Model):
    name=models.CharField(
        max_length=254,
        default='',
        blank=True
    )
    description=models.CharField(
        max_length=254,
        default='',
        blank=True
    )
    parameter=models.CharField(
        max_length=254,
        default='',
        blank=True
    )
    updated_date=models.DateTimeField(
        blank=True,
        auto_now=True
    )
    created_date=models.DateTimeField(
        blank=True,
        auto_now_add=True
    )