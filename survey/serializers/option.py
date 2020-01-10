from rest_framework import serializers
from ..models import Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["id", "description", "question"]

    def validate(self, data):
        request = self.context.get("request")
        code = request.query_params.get("creator__key")
        if code is None:
            return serializers.ValidationError("Request must have the user key")

        return data
