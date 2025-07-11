from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

class SoftDeleteQuerySet(QuerySet):
    def delete(self):
        super(SoftDeleteQuerySet, self).update(object_status = -1)
    def hard_delete(self):
        super(SoftDeleteQuerySet, self).delete()

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model).filter(object_status = 1)
    def all_objects(self):
        return SoftDeleteQuerySet(self.model)
    def deleted_objects(self):
        return SoftDeleteQuerySet(self.model).filter(object_status = -1)


class Committee(models.Model):
    name = models.CharField(max_length=255)  # e.g., "Local Organizing Committee"
    description = models.TextField(blank=True, null=True)
    object_status = models.IntegerField(default = 1)
    objects = SoftDeleteManager()
    
    def delete(self, using=None, keep_parents=False):
        self.object_status = -1
        self.save()

    def __str__(self):
        return self.name

class CommitteeMember(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255)
    role = models.CharField(max_length=100, blank=True)  # e.g., Chair, Co-Chair
    image_path = models.ImageField(upload_to='committee_members/')
    profile_link = models.URLField(blank=True, null=True)
    bio_data = models.FileField(blank=True, null=True)
    order  = models.PositiveIntegerField(default=99)
    added_on = models.DateTimeField(auto_now = True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    object_status = models.IntegerField(default = 1)
    objects = SoftDeleteManager()

    def delete(self, using=None, keep_parents=False):
        self.object_status = -1
        self.save()

    class Meta:
        ordering = ["committee", "order"]
    
    def __str__(self):
        return f"{self.name} ({self.committee.name})"

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=100, blank=True)  # e.g., "Keynote Speaker"
    bio_data = models.FileField(blank=True, null=True)
    image_path = models.ImageField(max_length=500, blank=True)
    link = models.URLField(blank=True)  # e.g., personal website, LinkedIn, etc.
    order  = models.PositiveIntegerField(default=99)
    added_on = models.DateTimeField(auto_now = True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    object_status = models.IntegerField(default = 1)
    objects = SoftDeleteManager()

    def delete(self, using=None, keep_parents=False):
        self.object_status = -1
        self.save()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
