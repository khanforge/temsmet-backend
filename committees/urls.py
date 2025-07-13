from rest_framework.routers import DefaultRouter
from .views import CommitteeMemberViewSet, SpeakerViewSet

router = DefaultRouter()
router.register(r"members", CommitteeMemberViewSet)
router.register(f"speakers", SpeakerViewSet)

urlpatterns = router.urls