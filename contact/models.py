from django.db import models
from core.models import AbstractModel
# Create your models here.
class Message(AbstractModel):
    name = models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Name"
    )
    mail= models.EmailField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Mail"
    )
    subject= models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Subject")
    message= models.TextField(
        default='',
        blank=True,
        verbose_name="Text"
    )
    def __str__(self):
        return f"Message: {self.mail}"
