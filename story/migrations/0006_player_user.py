# Generated by Django 2.0.13 on 2019-03-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_auto_20190318_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
