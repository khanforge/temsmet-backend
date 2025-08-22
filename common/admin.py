from django.contrib import admin
from .models import LatestUpdates, Page, ConferenceEvent

# Register your models here.
class LatestUpdateAdmin(admin.ModelAdmin):
    list_display = ["news", 'live', "order", "priority", "priority_colors"]
    list_editable = ['live', "order", "priority", "priority_colors"]

class PageAdmin(admin.ModelAdmin):
    list_display = ['name', 'enabled']
    list_editable = ['enabled']

class ConfereceEventAdmin(admin.ModelAdmin):
    list_display = ["name", "prev_date", "updated_date", "is_firm_deadline"]
    list_editable = ["prev_date", "updated_date", "is_firm_deadline"]

admin.site.register(LatestUpdates, LatestUpdateAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(ConferenceEvent, ConfereceEventAdmin)