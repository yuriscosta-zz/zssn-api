# Generated by Django 2.2.4 on 2019-08-14 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20190814_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survivor',
            name='last_location',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Location'),
        ),
    ]