from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SponsorDetail
from .serializers import SponsorSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class SponsorshipDetailsVeiwSet(ModelViewSet):
    serializer_class = SponsorSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company_name'] 

    def get_queryset(self):
        queryset = SponsorDetail.objects.all()
        tier_name = self.request.query_params.get("tier_name")
        position = self.request.query_params.get("position")
        if tier_name:
            queryset = queryset.filter(tier__sponsor_tier = tier_name)
        if position:
            queryset = queryset.filter(position = position)
        queryset = queryset.order_by("order")
        return queryset