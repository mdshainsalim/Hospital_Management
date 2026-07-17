from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = "__all__"
        read_only_fields = ["total_amount"]

    def validate(self, attrs):
        consultation_fee = attrs.get("consultation_fee")
        discount = attrs.get("discount", 0)

        if discount > consultation_fee:
            raise serializers.ValidationError(
                "Discount cannot be greater than consultation fee."
            )

        return attrs