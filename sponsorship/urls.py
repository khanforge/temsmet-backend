from rest_framework.routers import DefaultRouter
from .views import SponsorshipDetailsVeiwSet

router = DefaultRouter()
router.register(r"", SponsorshipDetailsVeiwSet, basename='sponsor')

urlpatterns = router.urls
