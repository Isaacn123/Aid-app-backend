from rest_framework import serializers
from .models import Events, EventCategory


class EventSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Events
        fields = ('organization','category','event_id','event_name','event_description', 'event_media', 'event_amount','amount_donated')

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ('category_id','category_name', 'category_description')