from django.db import models

from .question import Question
from .option import Option
from .form import Form
from user.models import User


class Answer(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="option")

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
