from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'gender', 'region', 'income_group', 'is_married',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.income_group:
            representation['income_group'] = self.get_income_group_display(
                instance.income_group)
        if instance.region:
            representation['region'] = self.get_region_display(instance.region)
        if instance.gender:
            representation['gender'] = self.get_gender_display(instance.gender)
        return representation

    def get_income_group_display(self, obj):
        choices = Customer.INCOME_GROUP_CHOICES
        choices = dict(choices)
        if choices.get(str(obj), None):
            return choices[str(obj)]
        return obj

    def get_region_display(self, obj):
        choices = Customer.REGION_CHOICES
        choices = dict(choices)
        if choices.get(str(obj), None):
            return choices[str(obj)]
        return obj

    def get_gender_display(self, obj):
        choices = Customer.GENDER_CHOICES
        choices = dict(choices)
        if choices.get(str(obj), None):
            return choices[str(obj)]
        return obj
