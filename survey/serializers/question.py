from rest_framework import serializers
from ..models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "description", "form"]

    def validate(self, data):
        request = self.context.get("request")
        code = request.query_params.get("creator__key")
        if code is None:
            return serializers.ValidationError("Request must have the user key")

        return data
