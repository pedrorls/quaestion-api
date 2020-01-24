from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ..serializers import QuestionSerializer
from ..models import Question, Form
from ..permissions import IsUserCodeSupplied
from ..filterset import BelongsToForm


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsUserCodeSupplied,)
    filter_backends = (DjangoFilterBackend, BelongsToForm)
    filter_fields = ("form__id",)
