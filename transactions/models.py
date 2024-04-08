from django.db import models
from events.models import Events
from core.models import TimestampedModel
import uuid

class Transactions(TimestampedModel):
    event_id = models.CharField(max_length=225)
    transaction_uid = models.UUIDField(default=uuid.uuid4, editable=False)
    user_id = models.IntegerField(blank=True, null=True)
    payment_id = models.CharField(max_length=225, null=True)
    organisation_id = models.IntegerField(max_length=225, null=True)
    transaction_amount = models.IntegerField(blank=True, null=True)
    original_amount = models.IntegerField(blank=True, null=True)
    is_partial = models.BooleanField(default=False)
    currency_code = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    merchant_reference_id = models.CharField(max_length=100, blank=True, null=True)
    customer_token = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=200)

    def __str__(self):
        return str(self.transaction_uid)