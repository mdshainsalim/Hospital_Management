from rest_framework import serializers
from .models import Appointment
from datetime import date


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ["patient"]

    def validate_appointment_date(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                "Appointment date cannot be in the past."
            )
        return value