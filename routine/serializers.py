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

class RoutineRequestForOneSerializer(serializers.Serializer):
    account_id = serializers.IntegerField(required = True)
    routine_id = serializers.IntegerField(required = True)
    
class RoutineListReqSerializer(serializers.Serializer):
    account_id = serializers.IntegerField(Required = True)
    today = serializers.DateField(Required = True)