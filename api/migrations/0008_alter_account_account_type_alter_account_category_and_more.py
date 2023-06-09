# Generated by Django 4.2.1 on 2023-05-04 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_invoice_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[(1, 'Compartilhada'), (2, 'Exclusiva')], default=2, max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='category',
            field=models.CharField(choices=[(1, 'Eletricidade'), (2, 'Água'), (3, 'Gás'), (4, 'Limpeza'), (5, 'Jardim'), (6, 'Outro')], default=6, max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_value',
            field=models.FloatField(default=0.0),
        ),
    ]
