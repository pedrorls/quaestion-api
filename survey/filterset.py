from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

from .models import Question

class IsFormCreator(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        code = request.query_params.get("code")
        return queryset.filter(creator__key=code)

class BelongsToForm(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        form_id = request.query_params.get("form_id")
        return queryset.filter(form__id=form_id)


class BelongsToQuestion(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        question_id = request.query_params.get("question_id")
        return queryset.filter(question__id=question_id)


class BelongsToCreatorOrForm(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        code = request.query_params.get("code")
        form_id = request.query_params.get("form_id")
        return queryset.filter(Q(creator__key=code)|Q(form__id=form_id))