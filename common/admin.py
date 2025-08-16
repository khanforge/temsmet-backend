from django.contrib import admin
from .models import LatestUpdates, Page

# Register your models here.
class LatestUpdateAdmin(admin.ModelAdmin):
    list_display = ["id", "news", 'live', "order", "priority", "priority_colors"]
    list_editable = ['live', "order", "priority", "priority_colors"]

class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'enabled']
    list_editable = ['enabled']



admin.site.register(LatestUpdates, LatestUpdateAdmin)
admin.site.register(Page, PageAdmin)