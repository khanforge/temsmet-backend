from rest_framework.routers import DefaultRouter
from .views import CommitteeMemberViewSet

router = DefaultRouter()
router.register(r"members", CommitteeMemberViewSet)

urlpatterns = router.urls