from rest_framework import routers
from survey.viewsets import FormView

router = routers.DefaultRouter()
router.register(r"forms", FormView, base_name="forms")

