# Generated by Django 4.2.1 on 2023-05-04 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_expense_remove_invoiceitem_account_delete_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.IntegerField(choices=[(1, 'Energia'), (2, 'Água'), (3, 'Gás'), (4, 'Limpeza'), (5, 'Jardim'), (6, 'Outro')], default=6),
        ),
    ]
