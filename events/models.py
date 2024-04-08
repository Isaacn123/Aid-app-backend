
import uuid
from django.db import models
from core.models import TimestampedModel
from organization.models import Organization

# Create your models here.


class EventCategory(TimestampedModel):
    category_id = models.UUIDField(default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(max_length=200)

    def __str__(self):
        return self.category_name


class Events(TimestampedModel):
    event_id = models.UUIDField(default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, blank=True, null=True)
    event_name = models.CharField(max_length=100)
    event_description = models.TextField(max_length=200)
    event_media = models.CharField(max_length=1000)
    event_amount = models.CharField(max_length=100)
    amount_donated = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.event_name




