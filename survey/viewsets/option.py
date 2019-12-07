from rest_framework import viewsets
from ..models import Option
from ..serializers import OptionSerializer


class OptionViewSet(viewsets.ModelViewSet):

    queryset = Option.objects.all()
    serializer_class = OptionSerializer

    def get_queryset(self):
        question = self.request.query_params.get("question", None)
        if question is not None:
            return Option.objects.filter(question=question)
