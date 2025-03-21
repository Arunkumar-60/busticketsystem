from rest_framework import serializers
from .models import Bus, Booking

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'  # Serialize all fields from the Bus model

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Serialize all fields from the Booking model
