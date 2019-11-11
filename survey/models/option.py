from django.db import models
from .question import Question


class Option(models.Model):
    description = models.CharField(max_length=150)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question"
    )

    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"

    def __str__(self):
        return self.description
