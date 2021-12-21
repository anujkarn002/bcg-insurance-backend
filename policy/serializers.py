from rest_framework import serializers
from .models import Policy, Vehicle

from customer.serializers import CustomerSerializer


class StatSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()
    total_premium = serializers.IntegerField()
    month = serializers.DateField()



class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('segment', 'fuel_type')


class PolicySerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    vehicle = VehicleSerializer(read_only=True)
    # premium should be less than 1 million
    premium = serializers.IntegerField(min_value=0, max_value=1000000)
    date_purchased = serializers.DateField(format='%m-%d-%Y', read_only=True)

    class Meta:
        model = Policy
        fields = ('id', 'customer', 'customer_is_married', 'vehicle', 'date_purchased', 'premium',
                  'bodily_injury', 'personal_injury', 'property_damage', 'collision', 'comprehensive')
        read_only_fields = ('id', 'customer', 'date_purchased')

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)