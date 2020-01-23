from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Answer
from ..serializers import AnswerSerializer
from ..permissions import IsUserCodeSupplied


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsUserCodeSupplied,)
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "creator__key",
        "question__id",
        "form__id",
    ]

