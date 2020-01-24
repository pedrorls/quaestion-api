from rest_framework.filters import BaseFilterBackend

from .models import Form

class IsFormCreator(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        code = request.query_params.get("code")
        return queryset.filter(creator__key=code)

class BelongsToCreatedForm(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        code = request.query_params.get("code")
        form_id = request.query_params.get("form_id")

        form = Form.objects.get(creator__key=code, id=form_id)
        return queryset.filter(form=form)