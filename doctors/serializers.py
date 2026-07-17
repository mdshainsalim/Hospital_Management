from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"

    def validate_visiting_fee(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Visiting fee must be greater than 0."
            )
        return value

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Doctor name must be at least 3 characters."
            )
        return value