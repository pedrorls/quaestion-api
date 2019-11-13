from rest_framework import routers
from survey.viewsets import FormViewset, QuestionViewSet, OptionViewSet, AnswerViewSet

router = routers.DefaultRouter()
router.register(r"forms", FormViewset)
router.register(r"questions", QuestionViewSet)
router.register(r"options", OptionViewSet)
router.register(r"options", AnswerViewSet)

