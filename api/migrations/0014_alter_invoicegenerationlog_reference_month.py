# Generated by Django 4.2.1 on 2023-05-04 03:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_apartment_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicegenerationlog',
            name='reference_month',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
