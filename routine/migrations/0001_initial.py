# Generated by Django 3.2.13 on 2022-04-21 07:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.reverse_related
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('routine_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('MIRACLE', '기상 관련'), ('HOMEWORK', '숙제 관련')], max_length=50)),
                ('is_alarm', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2022, 4, 21, 7, 29, 7, 258707, tzinfo=utc))),
                ('modified_at', models.DateTimeField(default=None)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.fields.reverse_related.ManyToOneRel, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoutineResult',
            fields=[
                ('routine_result_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('result', models.CharField(choices=[('NOT', '안함'), ('TRY', '시도'), ('DONE', '완료')], max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 4, 21, 7, 29, 7, 258707, tzinfo=utc))),
                ('modified_at', models.DateTimeField(default=None)),
                ('routine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
        ),
        migrations.CreateModel(
            name='RoutineDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 4, 21, 7, 29, 7, 259707, tzinfo=utc))),
                ('modified_at', models.DateTimeField(default=None)),
                ('routine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
        ),
    ]
