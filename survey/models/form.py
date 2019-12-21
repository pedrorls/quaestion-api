from django.db import models
from django.utils import timezone

from user.models import User


class Form(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "form"
        verbose_name_plural = "forms"

    def __str__(self):
        return self.title
