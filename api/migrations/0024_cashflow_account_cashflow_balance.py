# Generated by Django 4.2.1 on 2023-05-04 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_expense_account_payment_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashflow',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cashflow',
            name='balance',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
