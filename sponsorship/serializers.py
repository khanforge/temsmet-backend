from rest_framework import serializers
from .models import SponsorDetail, Tier

class SponsorSerializers(serializers.ModelSerializer):
    tier_name = serializers.CharField(source="tier.sponsor_tier")

    class Meta:
        model = SponsorDetail
        fields = [
            "id",
            "company_name",
            "link",
            "logo",
            "tier_name",
            "position",
            "order"
        ]