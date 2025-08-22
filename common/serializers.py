from rest_framework import serializers
from common.models import LatestUpdates, Page, ConferenceEvent
from datetime import date

class LatestUpdatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = LatestUpdates
        fields = "__all__"

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields =  "__all__"


class ConferenceEventSerializer(serializers.ModelSerializer):
    highlight = serializers.SerializerMethodField()
    
    class Meta:
        model = ConferenceEvent
        fields = ["id", "name", "prev_date", "updated_date", "is_firm_deadline", "highlight"]

    def get_highlight(self, obj):
        today = date.today()
        upcoming_events = ConferenceEvent.objects.filter(updated_date__gte=today).order_by("updated_date")
        if upcoming_events.exists() and obj.id == upcoming_events.first().id:
            return "red"
        return "normal"
