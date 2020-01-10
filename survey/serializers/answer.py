from rest_framework import serializers
from ..models import Answer, Form, Question, Option


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "creator", "form", "question", "option"]

    def validate(self, data):
        request = self.context.get("request")
        code = request.query_params.get("creator__key", None)

        question = Question.objects.get(id=data["question"].id)
        option = Option.objects.get(id=data["option"].id)
        form = Form.objects.get(id=question.form.id)

        if code is None:
            return serializers.ValidationError("Request must have the user key")

        if form.id != data["form"].id:
            raise serializers.ValidationError(
                "Question does not belong to the chosen form"
            )

        if question.id != option.question.id:
            raise serializers.ValidationError(
                "Option does not belong to the chosen question"
            )

        return data

