from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Answer
from ..serializers import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "creator__username",
        "question__id",
        "form__id",
    ]
