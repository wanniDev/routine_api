from unittest import result
from unittest.mock import create_autospec
from account.models import CustomUser
from django.db import models
from django.utils import timezone

CATEGORY_CHOICES = (
    ('MIRACLE', '기상 관련'),
    ('HOMEWORK', '숙제 관련')
)
RESULT_CHOICES = (
    ('NOT', '안함'),
    ('TRY', '시도'),
    ('DONE', '완료')
)

class Routine(models.Model):
    routine_id = models.AutoField(primary_key=True) #pk
    account_id = models.ForeignKey(CustomUser, on_delete=models.ManyToOneRel) #fk
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES) #enum(MIRACLE(기상 관련), HOMEWORK(숙제 관련))
    is_alarm = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    create_at = models.DateField(default=timezone.now())
    modified_at = models.DateField(default=timezone.now())
    
class RoutineResult(models.Model):
    routine_result_id = models.AutoField(primary_key=True) #pk
    routine_id = models.ForeignKey(Routine, to_field='routine_id', on_delete=models.CASCADE)  #fk
    result  = models.CharField(max_length=50, choices=RESULT_CHOICES)  #enum(NOT(안함), TRY(시도), DONE(완료))
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now())
    modified_at = models.DateField(default=timezone.now())
    
class RoutineDay(models.Model):
    day = models.CharField(max_length=3)
    routine_id = models.ForeignKey(Routine, to_field='routine_id', on_delete=models.CASCADE)  #fk
    created_at = models.DateField(default=timezone.now()) #시간
    modified_at = models.DateField(default=None) #시간