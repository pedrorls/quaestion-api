from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Form
from ..serializers import FormSerializer
from ..permissions import IsCreator


class FormViewset(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["creator__username"]
