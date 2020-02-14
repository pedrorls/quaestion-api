from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Answer
from ..serializers import AnswerSerializer
from ..permissions import IsUserCodeSupplied
from ..filterset import BelongsToCreatorOrForm

class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all().prefetch_related("form", "question", "creator")
    serializer_class = AnswerSerializer
    permission_classes = (IsUserCodeSupplied,)
    filter_backends = (
        DjangoFilterBackend, BelongsToCreatorOrForm
    )
    filterset_fields = (
        "creator__key",
        "form",
    )

