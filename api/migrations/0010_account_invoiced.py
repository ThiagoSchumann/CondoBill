# Generated by Django 4.2.1 on 2023-05-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_account_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='invoiced',
            field=models.BooleanField(default=False),
        ),
    ]
