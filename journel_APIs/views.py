from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Authors
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import AuthorsSerializer, UserSerializer,loginSerializer
# Create your views here.

    

class Registration(APIView):
     def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                username = serializer.validated_data.get("username")
                password = serializer.validated_data.get("password")
                user = authenticate(request, username=username, password=password)
                refresh = RefreshToken.for_user(user)
                data={
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }
                return Response({"message": "Successful registration", "data":data}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({"error": "A user with this information already exists."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"username or email already exist","data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        data = request.data
        serializer = loginSerializer(data=data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            user = authenticate(request,username=username, password=password)
            if user is None:
                return Response({"message":"username or password does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                refresh = RefreshToken.for_user(user)
                data={
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }
                return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)