from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=25, null=True, blank=True, choices=GENDER_CHOICES)
    REGION_CHOICES = (
        ('east', 'East'),
        ('west', 'West'),
        ('north', 'North'),
        ('south', 'South'),
    )
    region = models.CharField(max_length=255, null=True, blank=True, choices=REGION_CHOICES)
    INCOME_GROUP_CHOICES = (
        ('1', '0- $25K'),
        ('2', '$25-$70K'),
        ('3', '>$70K'),
    )
    income_group = models.CharField(max_length=255, null=True, blank=True, choices=INCOME_GROUP_CHOICES)
    is_married = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

