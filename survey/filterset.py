from rest_framework.filters import BaseFilterBackend

from .models import Form

class IsFormCreator(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        code = request.query_params.get("code")
        return queryset.filter(creator__key=code)