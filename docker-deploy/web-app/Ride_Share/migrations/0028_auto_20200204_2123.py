# Generated by Django 2.2.9 on 2020-02-05 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ride_Share', '0027_auto_20200204_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredsharer',
            name='rideid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='registeredsharer',
            name='registered_sharer_id',
            field=models.IntegerField(null=True),
        ),
    ]