from django.db import models
from .form import Form


class Question(models.Model):
    description = models.CharField(max_length=50)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="form")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.description
