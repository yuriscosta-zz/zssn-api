# Generated by Django 2.2.4 on 2019-08-08 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20190808_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='survivor',
        ),
    ]