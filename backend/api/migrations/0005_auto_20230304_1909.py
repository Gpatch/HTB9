# Generated by Django 3.2.18 on 2023-03-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20230304_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='acousticness',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='danceability',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='energy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='instrumentalness',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='key',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='liveness',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='loudness',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='mode',
            field=models.IntegerField(choices=[(0, 'Minor'), (1, 'Major')], null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='speechiness',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='tempo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='time_signature',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='uri',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='valence',
            field=models.FloatField(null=True),
        ),
    ]
