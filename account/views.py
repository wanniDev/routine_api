from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from account.serializers import UserSerializer, TokenObtainPairSerializer

import re

class SignupView(APIView):
    http_method_names = ['post']

    permission_classes = (permissions.AllowAny,)

    def post(self, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            is_password_valid = re.fullmatch(r'^(?=.*[a-zA-Z0-9`~!@#$%^&*()\-_+=\\]).{8,}$', serializer.data['password']);
            if is_password_valid is None:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': 'You must input more than 8 alphanumeric characters with special numbers.'})
            # print(regex.match(serializer.data['password']))
            get_user_model().objects.create_user(**serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer