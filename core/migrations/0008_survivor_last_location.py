# Generated by Django 2.2.4 on 2019-08-08 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_remove_location_survivor'),
        ('core', '0007_remove_survivor_last_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='survivor',
            name='last_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Location'),
        ),
    ]