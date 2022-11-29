# Generated by Django 4.0.6 on 2022-11-29 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayName', models.CharField(max_length=255)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Places',
                'verbose_name_plural': 'Places',
            },
        ),
    ]
