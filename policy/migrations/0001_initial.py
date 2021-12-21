# Generated by Django 4.0 on 2021-12-20 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment', models.CharField(blank=True, max_length=255, null=True)),
                ('fuel_type', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_is_married', models.BooleanField(default=False)),
                ('date_purchased', models.DateField(blank=True, null=True)),
                ('premium', models.IntegerField(blank=True, null=True)),
                ('bodily_injury', models.BooleanField(default=False)),
                ('personal_injury', models.BooleanField(default=False)),
                ('property_damage', models.BooleanField(default=False)),
                ('collision', models.BooleanField(default=False)),
                ('comprehensive', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policies', to='customer.customer')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policies', to='policy.vehicle')),
            ],
        ),
    ]
