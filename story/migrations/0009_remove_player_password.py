# Generated by Django 2.0.13 on 2019-03-18 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0008_auto_20190318_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='password',
        ),
    ]
