from turtle import title
from typing_extensions import Required
from rest_framework import serializers
from .models import CATEGORY_CHOICES, RESULT_CHOICES, Routine, RoutineDay

class RoutineRequestSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)
    goal = serializers.CharField(required=False, allow_blank=True, max_length=200)
    is_alarm = serializers.BooleanField(required=False)
    days = serializers.ListField(required=False)

class RoutineIdSerializer(serializers.Serializer):
    routine_id = serializers.IntegerField()

class MessageSerializer(serializers.Serializer):
    msg = serializers.CharField(max_length=200)
    status = serializers.CharField(max_length=50)

class RoutineResponseSerializer(serializers.Serializer):
    data = RoutineIdSerializer()
    message = MessageSerializer()