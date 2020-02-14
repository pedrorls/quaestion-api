from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Form
from ..serializers import FormSerializer
from ..permissions import IsUserCodeSupplied
from ..filterset import IsFormCreator
from user.models import User


class FormViewset(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (IsUserCodeSupplied,)
    filter_backends = (IsFormCreator,)
    filter_fields = ("creator__key",)

    def perform_create(self, serializer):
        code = self.request.query_params.get("code", None)
        try:
            user = User.objects.get(key=code)
            serializer.save(creator=user)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

