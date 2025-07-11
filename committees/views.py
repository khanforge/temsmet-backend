from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import CommitteeMember
from .serializers import CommitteeMemberSerializer
# Create your views here.

class CommitteeMemberViewSet(ModelViewSet):
    queryset = CommitteeMember.objects.all().order_by("committee", "order")
    serializer_class = CommitteeMemberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['committee'] 