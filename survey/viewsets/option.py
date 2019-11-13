from rest_framework import viewsets
from ..models import Option
from ..serializers import OptionSerializer

class OptionViewSet(viewsets.ModelViewSet):

    queryset = Option.objects.all()
    serializer_class = OptionSerializer