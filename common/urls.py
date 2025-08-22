from django.urls import path
from .views import LatestUpdateView, PageConfigView, ConferenceEventViewSet


urlpatterns = [
    path('latest-updates/', LatestUpdateView.as_view(), name="latest_update_veiw"),
    path("pages/", PageConfigView.as_view(), name="page-config"),
    path('important-dates/', ConferenceEventViewSet.as_view(), name="conference-events" )
]
