# Generated by Django 2.2.9 on 2020-01-29 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ride_Share', '0005_auto_20200128_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(choices=[('con', 'Convertible'), ('cou', 'Coupe'), ('sed', 'Sedan'), ('suv', 'SUV'), ('tru', 'Truck')], max_length=10),
        ),
    ]
