# Generated by Django 4.2.1 on 2023-05-04 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_invoicegenerationlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('shared', 'Compartilhada'), ('exclusive', 'Exclusiva')], max_length=20),
        ),
    ]
