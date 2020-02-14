from rest_framework import serializers
from ..models import Question, Form
from user.models import User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "description", "form"]


    def validate(self, data):
        request = self.context["request"]
        code = request.query_params.get("code", None)
        form_id = data["form"].id
        forms = Form.objects.filter(creator__key=code).values_list("id", flat=True)

        if form_id not in forms:
            raise serializers.ValidationError(
                "Selected form does not belong to you"
            )
        
        return data

