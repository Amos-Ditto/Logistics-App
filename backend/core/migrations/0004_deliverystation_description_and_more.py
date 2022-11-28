# Generated by Django 4.0.6 on 2022-11-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_deliverystation_deliverymanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverystation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deliverystation',
            name='region',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='deliverystation',
            name='town',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]