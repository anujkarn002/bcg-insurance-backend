import csv
from django.core.management.base import BaseCommand
from django.db.models import Count
from policy.models import Policy, Vehicle
from customer.models import Customer
from datetime import timedelta, datetime
from django.utils.timezone import utc


class Command(BaseCommand):
    help = 'Loads data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='CSV file')

    def get_income_group_key(self, income_group):
        if income_group == '0- $25K':
            return '1'
        elif income_group == '$25-$70K':
            return '2'
        else:
            return '3'

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']
        self.stdout.write(self.style.SUCCESS(
            'Started loading csv file. This may take 5-7 minutes.'))
        start_time = datetime.now()
        file = open(file_path, 'r')
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            # Get customer and policy fields value
            policy_id = int(row[0])  # Policy ID
            date_purchased = datetime.strptime(
                row[1], '%m/%d/%Y').date()  # Date Purchased
            customer_id = int(row[2])  # Customer ID
            fuel_type = row[3]  # Fuel Type
            segment = row[4].upper()  # Vehicle Segment
            premium = int(row[5])  # Premium
            body_injury = True if row[6] == "1" else False  # Bodily Injury
            personal_injury = True if row[7] == "1" else False  # Personal Injury
            property_damage = True if row[8] == "1" else False  # Property Damage
            collision = True if row[9] == "1" else False  # Collision
            comprehensive = True if row[10] == "1" else False  # Comprehensive
            gender = row[11].lower()  # Customer Gender
            income_group = self.get_income_group_key(
                row[12])  # Customer Income Group
            region = row[13].lower()  # Customer Region
            # Customer Marital Status
            is_married = True if row[14] == "1" else False

            # Customer
            customer, created = Customer.objects.get_or_create(pk=customer_id,)
            if created:
                customer.income_group = income_group
                customer.gender = gender
                customer.region = region
                customer.is_married = is_married
                customer.save()

            # Vehicle
            vehicle, created = Vehicle.objects.get_or_create(
                fuel_type=fuel_type, segment=segment)

            # Policy
            policy = Policy.objects.create(pk=policy_id, customer=customer, customer_is_married=is_married, vehicle=vehicle, date_purchased=date_purchased, premium=premium,
                                           bodily_injury=body_injury, personal_injury=personal_injury, property_damage=property_damage, collision=collision, comprehensive=comprehensive)

        # finish loading data
        end_time = datetime.now()
        self.stdout.write(self.style.SUCCESS(
            'Successfully loaded data from CSV file.'))
        self.stdout.write(self.style.SUCCESS(
            'Time taken (in seconds): {}'.format((end_time - start_time).total_seconds())))
        self.stdout.write(self.style.SUCCESS('Time taken (in minutes): {}'.format(
            (end_time - start_time).total_seconds() / 60)))
