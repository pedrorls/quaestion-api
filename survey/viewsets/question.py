from rest_framework import viewsets
from ..serializers import QuestionSerializer
from ..models import Question, Form


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        key = self.request.query_params.get("creator__key", None)
        form = self.request.query_params.get("form__id", None)
        if key and form:
            forms = Form.objects.filter(creator__key=key)
            return Question.objects.filter(form__in=forms)
