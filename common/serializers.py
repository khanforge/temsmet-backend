from rest_framework import serializers
from common.models import LatestUpdates, Page

class LatestUpdatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = LatestUpdates
        fields = "__all__"

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields =  "__all__"