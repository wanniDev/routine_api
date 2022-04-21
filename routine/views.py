from unicodedata import category
from django.shortcuts import render
from rest_framework.response import Response


from .models import CustomUser, Routine, RoutineResult, RoutineDay
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from .serializers import RoutineListReqSerializer, RoutineRequestSerializer, RoutineIdSerializer, RoutineRequestForOneSerializer 
from rest_framework_simplejwt.tokens import AccessToken

# routine 추가
class CreateRoutineView(APIView) :
    http_method_names = ['post']
    
    permission_classes = (permissions.AllowAny,)
    
    def post(self, *args, **kwargs) :
        serializer = RoutineRequestSerializer(data = self.request.data)
        
        if serializer.is_valid():
            jwt_token = self.request.headers.get('Authorization')
            access_token_obj = AccessToken(jwt_token)
            user_id = access_token_obj['user_id']
            user = CustomUser.objects.get(id = user_id)
            routine = Routine.objects.create(account_id=user,
                                   title=serializer.data['title'],
                                   category=serializer.data['category'],
                                   is_alarm=serializer.data['is_alarm']
                                   )
            RoutineResult.objects.create(routine_id=routine,
                                         result='NOT'
                                         )
            return Response(status=status.HTTP_201_CREATED, data = {
                'data' : {
                    'routine_id' : routine.routine_id
                },
                'message' : {
                    'msg' : ' .', 'status' : 'ROUTINE_CREATE_OK'
                }
            })
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

# routine 단건 조회
class RoutineView(APIView) :
    http_method_names = ['get']

    permission_classes = (permissions.AllowAny,)
    
    def get(self, *args, **kwargs):
        serializer = RoutineRequestForOneSerializer(data=self.request.data)
        if serializer.is_valid():
            jwt_token = self.request.headers.get('Authorization')
            access_token_obj = AccessToken(jwt_token)
            user_id = access_token_obj['user_id']
            user = CustomUser.objects.get(id = user_id)
            if user is not None and user.id == user_id :
                routine = Routine.objects.get(account_id = user_id, routine_id=serializer.data['routine_id'])
                routine_result = RoutineResult.objects.get(routine_id = routine.routine_id)
                return Response(status=status.HTTP_201_CREATED, data = {
                    'data' : {
                        'id' : routine.routine_id,
                        'result' : routine_result.result,
                        'title' : routine.title
                    },
                    'message' : {
                        'msg' : ' .', 'status' : 'ROUTINE_DETAIL_OK'
                    }
                })
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        
# routine 목록 조회
class RoutineListView(APIView) :
    http_method_names = ['get']

    permission_classes = (permissions.AllowAny,)
    
    def get(self, *args, **kwargs) :
        serializer = RoutineListReqSerializer(data=self.request.data)
        if serializer.is_valid():
            jwt_token = self.request.headers.get('Authorization')
            access_token_obj = AccessToken(jwt_token)
            user_id = access_token_obj['user_id']
            user = CustomUser.objects.get(id = user_id)
            results = []
            if user is not None and user.id == user_id :
                routines = Routine.objects.filter(account_id = user, create_at = serializer.data['today'])
                for routine in routines :
                    results.append(
                        {
                            'id' : routine.routine_id,
                            "title" : routine.title
                        }
                    )
                