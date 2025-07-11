from django.contrib import admin
from .models import Committee, CommitteeMember, Speaker
# Register your models here.

admin.site.site_header = "Conference CMS Admin"
admin.site.site_title = "Conference Management"
admin.site.index_title = "Manage Conference Committees and Members"


class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'committee', 'affiliation', 'order']
    list_editable = ['order', 'affiliation']
    ordering = ['committee', 'order']
    list_filter = ['committee']
    search_fields = ['name', 'role']

    def get_queryset(self, request):
        return CommitteeMember.objects.all_objects()

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'affiliation', 'order']
    list_editable = ['order', 'affiliation']
    ordering = ['order']
    search_fields = ['name', 'role']
    def get_queryset(self, request):
        return CommitteeMember.objects.all_objects()

admin.site.register(Committee)
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(Speaker, SpeakerAdmin)