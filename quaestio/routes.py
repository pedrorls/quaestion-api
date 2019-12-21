from rest_framework import routers
from survey.viewsets import FormViewset, QuestionViewSet, OptionViewSet, AnswerViewSet
from user.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r"forms", FormViewset)
router.register(r"questions", QuestionViewSet)
router.register(r"options", OptionViewSet)
router.register(r"answers", AnswerViewSet)
router.register(r"users", UserViewSet)
