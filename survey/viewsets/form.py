from rest_framework import viewsets
from ..models import Form
from survey.serializers import FormSerializer

class FormView(viewsets.ModelViewSet):
    lookup_fields = "id"
    serializer_class = FormSerializer

    def get_queryset(self):
        return Form.objects.all()
