from rest_framework import serializers
from ..models import Answer, Form, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "creator", "form", "question", "option"]

    def validate(self, data):
        question = Question.objects.get(id=data["question"].id)
        form = Form.objects.get(id=question.form.id)

        print(form)

        if form.id != data["form"].id:
            raise serializers.ValidationError(
                "Question does not belong to the chosen form"
            )

        return data

