from rest_framework import viewsets
from ..serializers import QuestionSerializer
from ..models import Question, Form


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        if username is not None:
            forms = Form.objects.filter(creator__username=username)
            return Question.objects.filter(form__in=forms)
