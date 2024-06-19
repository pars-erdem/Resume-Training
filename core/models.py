from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True
    )
    class Meta:
        abstract = True
class GeneralSetting(AbstractModel):
    name=models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Name"
    )
    description=models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Description"

    )
    parameter=models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Parameter"
    )

    def __str__(self):
        return f"General Setting: {self.name}"
class ImageSetting(AbstractModel):
    name = models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Name"
        )
    description = models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Description"
        )
    file = models.ImageField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="images/",
        )

    def __str__(self):
        return f"İmage Setting: {self.name}"
class Skill(AbstractModel):
    order=models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    name = models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Name"
        )
    percentage=models.IntegerField(
        default=20,
        verbose_name="Percentage",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    def __str__(self):
        return f"Skill: {self.name}"