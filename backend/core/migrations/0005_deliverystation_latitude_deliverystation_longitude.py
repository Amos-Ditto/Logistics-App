# Generated by Django 4.0.6 on 2022-11-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_deliverystation_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverystation',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='deliverystation',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
