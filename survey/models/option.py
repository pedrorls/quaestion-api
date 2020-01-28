from django.db import models
from .question import Question


class Option(models.Model):
    VERY_BAD = "Very bad"
    BAD = "Bad"
    NEUTRAL = "Neutral"
    GOOD = "Good"
    VERY_GOOD = "Very good"

    CHOICES = [
        (VERY_BAD, VERY_BAD),
        (BAD, BAD),
        (NEUTRAL, NEUTRAL),
        (GOOD, GOOD),
        (VERY_GOOD, VERY_GOOD)
    ]
    description = models.CharField(max_length=15, choices=CHOICES, default=NEUTRAL)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question"
    )

    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"
        unique_together = ("description", "question")

    def __str__(self):
        return self.description
