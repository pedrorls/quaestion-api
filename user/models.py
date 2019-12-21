import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    key = models.CharField(max_length=50, default=uuid.uuid4(), unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

