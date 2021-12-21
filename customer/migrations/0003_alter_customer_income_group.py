# Generated by Django 4.0 on 2021-12-21 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_income_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='income_group',
            field=models.CharField(blank=True, choices=[('1', '0- $25K'), ('2', '$25-$70K'), ('3', '>$70K')], max_length=255, null=True),
        ),
    ]