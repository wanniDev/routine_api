# Generated by Django 3.2.13 on 2022-04-21 08:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0003_auto_20220421_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 8, 10, 17, 333423, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routineday',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 8, 10, 17, 334423, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routineresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 8, 10, 17, 333423, tzinfo=utc)),
        ),
    ]