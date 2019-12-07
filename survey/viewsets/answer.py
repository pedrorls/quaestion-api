from rest_framework import viewsets
from ..models import Answer
from ..serializers import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        if username is not None:
            return Answer.objects.filter(creator__username=username)
