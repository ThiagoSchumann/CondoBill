# Generated by Django 4.2.1 on 2023-05-04 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_invoicegenerationlog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.IntegerField(choices=[(1, 'Compartilhada'), (2, 'Exclusiva')], default=2),
        ),
    ]
