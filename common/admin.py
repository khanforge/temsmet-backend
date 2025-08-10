from django.contrib import admin
from .models import LatestUpdates

# Register your models here.
class LatestUpdateAdmin(admin.ModelAdmin):
    list_display = ["id", "news", 'live', "order", "priority", "priority_colors"]
    list_editable = ['live', "order", "priority", "priority_colors"]

admin.site.register(LatestUpdates, LatestUpdateAdmin)
 