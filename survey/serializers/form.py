from rest_framework import serializers
from ..models import Form


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            "id",
            "title",
            "description",
            "creator",
        ]

    def validate(self, data):
        request = self.context.get("request")
        code = request.query_params.get("creator__key")
        if code is None:
            return serializers.ValidationError("Request must have the user key")

        return data
