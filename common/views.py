from django.shortcuts import render
from common.models import LatestUpdates, Page
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView
from .serializers import LatestUpdatesSerializers, PageSerializer

# Create your views here.
class LatestUpdateView(ListAPIView):
    serializer_class = LatestUpdatesSerializers

    def get_queryset(self):
        return LatestUpdates.objects.filter(live = 1).order_by("order", "-created_at")

class PageConfigView(ListAPIView):
    serializer_class = PageSerializer
    def get_queryset(self):
        return Page.objects.all()