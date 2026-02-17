from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    group = models.CharField(max_length=1)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=30, blank=True)
    iconColor = models.CharField(max_length=7)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['fullname']

    def __str__(self):
        return self.fullname