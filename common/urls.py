from django.urls import path
from .views import LatestUpdateView

urlpatterns = [
    path('', LatestUpdateView.as_view(), name="latest_update_veiw"),
]
