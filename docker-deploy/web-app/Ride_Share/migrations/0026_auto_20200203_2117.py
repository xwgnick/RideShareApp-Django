# Generated by Django 2.2.9 on 2020-02-04 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ride_Share', '0025_auto_20200203_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(help_text='Required.', max_length=254, verbose_name='Email address'),
        ),
    ]
