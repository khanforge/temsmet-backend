from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import CommitteeMember, Speaker
from .serializers import CommitteeMemberSerializer, SpeakerSerialzer
# Create your views here.

class CommitteeMemberViewSet(ModelViewSet):
    queryset = CommitteeMember.objects.all().order_by("committee", "order")
    serializer_class = CommitteeMemberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['committee'] 

class SpeakerViewSet(ModelViewSet):
    queryset = Speaker.objects.all().order_by("order")
    serializer_class = SpeakerSerialzer
    permission_class = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']