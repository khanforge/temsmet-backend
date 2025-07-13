from rest_framework import serializers
from .models import CommitteeMember, Committee, Speaker

class CommitteeMemberSerializer(serializers.ModelSerializer):
    committee_name = serializers.CharField(source='committee.name', read_only=True)
    committee_id = serializers.IntegerField(source='committee.id', read_only=True)

    class Meta:
        model = CommitteeMember
        fields = [
            'id',
            'name',
            'affiliation',
            'role',
            'image_path',
            'profile_link',
            'bio_data',
            'committee_id',
            'committee_name',
        ]

class SpeakerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = "__all__"