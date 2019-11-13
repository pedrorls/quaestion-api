from rest_framework import viewsets
from ..models import Form
from ..serializers import FormSerializer

class FormViewset(viewsets.ModelViewSet):
    lookup_fields = "id"
    queryset = Form.objects.all()
    serializer_class = FormSerializer
