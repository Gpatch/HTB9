# Generated by Django 3.2.18 on 2023-03-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20230304_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='country',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
