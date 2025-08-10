from rest_framework import serializers
from common.models import LatestUpdates

class LatestUpdatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = LatestUpdates
        fields = "__all__"