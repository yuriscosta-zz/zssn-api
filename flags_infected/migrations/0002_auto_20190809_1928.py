# Generated by Django 2.2.4 on 2019-08-09 19:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flags_infected', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flaginfected',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]