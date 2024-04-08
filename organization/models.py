from lib2to3.refactor import MultiprocessingUnsupported
from operator import mod
from pyexpat import model
from django.db import models
from authenticate.models import User

from core.models import TimestampedModel
# Create your models here.
class Organization(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=100)
    organization_description = models.TextField()
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


    def __str__(self):
        return self.organization_name
    

