from django.contrib import admin
from .models import Tier, SponsorDetail
# Register your models here.

class TierManager(admin.ModelAdmin):
    list_display = ["sponsor_tier", 'cost_inr', "tier_order"]
    list_editable = ["tier_order"]

class SponsorDetailManager(admin.ModelAdmin):
    list_display = ["company_name", 'link', "tier", "position", "order"]
    list_editable = ['link', "tier", "position", "order"]


admin.site.register(Tier, TierManager)
admin.site.register(SponsorDetail, SponsorDetailManager)