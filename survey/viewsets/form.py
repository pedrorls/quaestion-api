from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Form
from ..serializers import FormSerializer
from ..permissions import IsUserCodeSupplied


class FormViewset(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (IsUserCodeSupplied,)

