from django.db import models

class LatestUpdates(models.Model):
    LIVE = 1
    INACTIVE = 0
    LIVE_STATUS = (
        (LIVE, "Live"),
        (INACTIVE, "Inactive")
    )
    IMPORTANT = "IMPORTANT"
    ANNOUNCEMENT = "ANNOUNCEMENT"
    NEWS = "NEWS"
    KEYNOTE_SPEAKER = "KEYNOTE SPEAKER"
    PRIORITY_CHOICES = (
        (IMPORTANT, "IMPORTANT"),
        (ANNOUNCEMENT, "ANNOUNCEMENT"),
        (NEWS, "NEWS"),
        (KEYNOTE_SPEAKER, "KEYNOTE SPEAKER"),
    )
    RED     = "red"
    GREEN   = "green"
    BLUE    = "blue"
    YELLOW  = "yellow"
    ORANGE  = "orange"
    PURPLE  = "purple"
    PINK    = "pink"
    TEAL    = "teal"
    BROWN   = "brown"
    GRAY    = "gray"
    BLACK   = "black"
    WHITE   = "white"

    COLOR_CHOICES = (
        (RED, "Red"),
        (GREEN, "Green"),
        (BLUE, "Blue"),
        (YELLOW, "Yellow"),
        (ORANGE, "Orange"),
        (PURPLE, "Purple"),
        (PINK, "Pink"),
        (TEAL, "Teal"),
        (BROWN, "Brown"),
        (GRAY, "Gray"),
        (BLACK, "Black"),
        (WHITE, "White"),
    )

    news = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=99)
    priority = models.CharField(choices=PRIORITY_CHOICES, default=IMPORTANT, max_length=20)
    priority_colors = models.CharField(choices=COLOR_CHOICES, default=RED, max_length=20)
    live = models.IntegerField(choices = LIVE_STATUS, default = LIVE)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"{self.news} - {self.id}"
    
class Page(models.Model):
    name = models.CharField(max_length=100, unique=True)   
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {'Enabled' if self.enabled else 'Disabled'}"

class ConferenceEvent(models.Model):
    name = models.CharField(max_length=255)   
    prev_date = models.DateField(null=True, blank=True)  
    updated_date = models.DateField()  
    is_firm_deadline = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    single_bed = models.CharField(max_length=100, blank=True, null=True)   
    double_bed = models.CharField(max_length=100, blank=True, null=True)   
    breakfast = models.BooleanField(default=False)      
    max_rooms = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    distance = models.CharField(max_length=50, blank=True, null=True)     
    address = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    suggestions = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=99)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
        ordering = ["name"]

    def __str__(self):
        return f"{self.id} - {self.name}"

class QuickLink(models.Model):
    RED     = "red"
    GREEN   = "green"
    BLUE    = "blue"
    YELLOW  = "yellow"
    ORANGE  = "orange"
    PURPLE  = "purple"
    PINK    = "pink"
    TEAL    = "teal"
    BROWN   = "brown"
    GRAY    = "gray"
    BLACK   = "black"
    WHITE   = "white"

    COLOR_CHOICES = (
        (RED, "Red"),
        (GREEN, "Green"),
        (BLUE, "Blue"),
        (YELLOW, "Yellow"),
        (ORANGE, "Orange"),
        (PURPLE, "Purple"),
        (PINK, "Pink"),
        (TEAL, "Teal"),
        (BROWN, "Brown"),
        (GRAY, "Gray"),
        (BLACK, "Black"),
        (WHITE, "White"),
    )

    target_choices = (
        ("_self", "Same Tab"),
        ("_blank", "New Tab"),
    )

    button_text = models.CharField(max_length = 100)
    button_colors = models.CharField(choices=COLOR_CHOICES, max_length=20)
    text_color = models.CharField(choices=COLOR_CHOICES, max_length=20, default="white")
    icon_svg = models.TextField(blank = True, null = True)
    target = models.CharField(choices = target_choices, default = "_self", max_length=10)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="Page_Name")
    link = models.URLField(max_length = 500, blank=True, null=True)
    order = models.PositiveIntegerField(default=99)
    is_live = models.BooleanField(default=True)
    file = models.FileField(upload_to = "quick_links_pdfs/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return f"{self.button_text}-{self.id}"