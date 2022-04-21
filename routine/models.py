from unittest import result
from unittest.mock import create_autospec
from account.models import CustomUser
from django.db import models
from django.utils import timezone

class Routine(models.Model):
    routine_id = models.BigIntegerField(primary_key=True) #pk
    account_id = models.ForeignKey(CustomUser, on_delete=models.ManyToOneRel) #fk
    title = models.CharField(max_length=200)
    CATEGORY_CHOICES = (
        ('MIRACLE', '기상 관련'),
        ('HOMEWORK', '숙제 관련')
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES) #enum(MIRACLE(기상 관련), HOMEWORK(숙제 관련))
    is_alarm = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    create_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(default=None)
    
class RoutineResult(models.Model):
    routine_result_id = models.BigIntegerField(primary_key=True) #pk
    routine_id = models.ForeignKey(Routine, on_delete=models.ManyToOneRel)  #fk
    RESULT_CHOICES = (
        ('NOT', '안함'),
        ('TRY', '시도'),
        ('DONE', '완료')
    )
    result  = models.CharField(max_length=50, choices=RESULT_CHOICES)  #enum(NOT(안함), TRY(시도), DONE(완료))
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(default=None)
    
class RoutineDay(models.Model):
    day
    routine_id  #fk
    created_at  #시간
    modified_at #시간