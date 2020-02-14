from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Option
from ..serializers import OptionSerializer
from ..permissions import IsUserCodeSupplied
from ..filterset import BelongsToQuestion


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = (IsUserCodeSupplied,)
    filter_fields = ("question",)
