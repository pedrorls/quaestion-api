from rest_framework import viewsets

from ..models import Form
from ..serializers import FormSerializer
from ..permissions import IsCreator


class FormViewset(viewsets.ModelViewSet):
    lookup_fields = "id"
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsCreator]

    def get_queryset(self):
        return Form.objects.filter(creator=self.request.user.id)
