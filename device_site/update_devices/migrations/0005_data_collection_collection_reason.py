# Generated by Django 4.0.2 on 2022-02-27 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update_devices', '0004_remove_data_collection_device_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_collection',
            name='collection_reason',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
