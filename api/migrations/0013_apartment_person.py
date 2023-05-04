# Generated by Django 4.2.1 on 2023-05-04 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_rename_owner_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.person'),
            preserve_default=False,
        ),
    ]
