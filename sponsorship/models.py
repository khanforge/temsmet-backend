from django.db import models

# Create your models here.
class Tier(models.Model):
    sponsor_tier = models.CharField(max_length=255)
    cost_inr = models.CharField(max_length=20, null=True, blank=True)
    exhibition_space = models.CharField(max_length=100, null=True, blank=True)
    stage_recognition = models.TextField(null=True, blank=True)
    promotional_coverage = models.TextField(null=True, blank=True)
    presentation_time = models.CharField(max_length=10, null=True, blank=True)
    tier_order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.sponsor_tier}"

class SponsorDetail(models.Model):
    TOP = 0
    SIDEBAR = 1
    POSITION_CHOICES = (
       ( TOP, "Top"),
       ( SIDEBAR, "Sidebar"),
    )
    company_name = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    tier = models.ForeignKey(Tier, null=True, blank=True, on_delete=models.SET_NULL)
    logo = models.ImageField(upload_to='sponsors/logos/', null=True, blank=True)
    position = models.IntegerField(choices=POSITION_CHOICES, default = SIDEBAR)
    order = models.IntegerField(default = 99)
    hieght = models.CharField(max_length=10, null=True, blank=True)
    width = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return f"{self.company_name}-{self.tier}-{self.id}"