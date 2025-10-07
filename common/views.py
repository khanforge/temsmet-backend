from django.shortcuts import render
from common.models import LatestUpdates, Page, ConferenceEvent, Hotel
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView
from .serializers import LatestUpdatesSerializers, PageSerializer, ConferenceEventSerializer, HotelSerializer
from rest_framework import viewsets
from django.db.models import IntegerField
from django.db.models.functions import Cast, Substr, Length

# Create your views here.
class LatestUpdateView(ListAPIView):
    serializer_class = LatestUpdatesSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return LatestUpdates.objects.filter(live = 1).order_by("order", "-created_at")

class PageConfigView(ListAPIView):
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Page.objects.all()

class ConferenceEventViewSet(ListAPIView):
    serializer_class = ConferenceEventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        return ConferenceEvent.objects.all().order_by("updated_date")

class HotelViewSet(ListAPIView):
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return (
            Hotel.objects.annotate(
                numeric_distance=Cast(
                    Substr("distance", 1, Length("distance") - 3),
                    IntegerField()
                )
            )
            .order_by("order", "numeric_distance", "name")
        )
