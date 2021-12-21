from django.db import models
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum, Q

# Create your models here.


class Vehicle(models.Model):
    segment = models.CharField(max_length=255, null=True, blank=True)
    fuel_type = models.CharField(max_length=255, null=True, blank=True)


class PolicyManager(models.Manager):
    def get_monthly_data(self, region=None):
        # get monthly count of policies, with region filter
        if not region:
            return self.annotate(month=TruncMonth('date_purchased')).values('month').annotate(total_count=Count('id'), total_premium=Sum('premium')).order_by()
        else:
            return self.filter(Q(customer__region=region)).annotate(month=TruncMonth('date_purchased')).values('month').annotate(total_count=Count('id'), total_premium=Sum('premium')).order_by()


class Policy(models.Model):
    class Meta:
        ordering = ('-id', '-date_purchased',)

    objects = PolicyManager()

    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(
        'customer.Customer', related_name='policies', on_delete=models.SET_NULL, null=True)
    customer_is_married = models.BooleanField(default=False)
    vehicle = models.ForeignKey(
        'Vehicle', related_name='policies', on_delete=models.SET_NULL, null=True)
    date_purchased = models.DateField(null=True, blank=True)
    premium = models.IntegerField(null=True, blank=True)
    bodily_injury = models.BooleanField(default=False)
    personal_injury = models.BooleanField(default=False)
    property_damage = models.BooleanField(default=False)
    collision = models.BooleanField(default=False)
    comprehensive = models.BooleanField(default=False)
