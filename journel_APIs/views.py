# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import IntegrityError
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate
# from .models import Authors,JournalModel
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User
# from .serializers import UserSerializer,loginSerializer,AuthorSerializer,JournalSerializer
# # Create your views here.

    

# class Registration(APIView):
#      def post(self, request):
#         data = request.data
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 username = serializer.validated_data.get("username")
#                 password = serializer.validated_data.get("password")
#                 user = authenticate(request, username=username, password=password)
#                 refresh = RefreshToken.for_user(user)
#                 data={
#                     'refresh':str(refresh),
#                     'access':str(refresh.access_token)
#                 }
#                 return Response({"message": "Successful registration", "data":data}, status=status.HTTP_201_CREATED)
#             except IntegrityError as e:
#                 return Response({"error": "A user with this information already exists."}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"message":"username or email already exist","data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# class LoginView(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = loginSerializer(data=data)
#         if serializer.is_valid():
#             username = serializer.validated_data.get("username")
#             password = serializer.validated_data.get("password")

#             user = authenticate(request,username=username, password=password)
#             if user is None:
#                 return Response({"message":"username or password does not exist"}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 refresh = RefreshToken.for_user(user)
#                 data={
#                     'refresh':str(refresh),
#                     'access':str(refresh.access_token)
#                 }
#                 return Response(data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.db import IntegrityError
from .models import Author, JournalModel
from django.contrib.auth.models import User
from .serializers import AuthorSerializer, JournalSerializer, UserSerializer, loginSerializer

class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class AuthorListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404

class AuthorDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Author, user_id=pk)

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class JournalListCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        journals = JournalModel.objects.all()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JournalDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
     return get_object_or_404(JournalModel, author__user_id=pk)
    
    def get(self, request, pk):
        journal = self.get_object(pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    def put(self, request, pk):
        journal = self.get_object(pk)
        serializer = JournalSerializer(journal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        journal = self.get_object(pk)
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                username = serializer.validated_data.get("username")
                password = serializer.validated_data.get("password")
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    author = Author.objects.create(user=user)
                    refresh = RefreshToken.for_user(user)
                    data = {
                        'access': str(refresh.access_token)
                    }
                    return Response({"user": user.id, "message": "Successful registration", "data": data}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "User authentication failed."}, status=status.HTTP_400_BAD_REQUEST)
            except IntegrityError as e:
                return Response({"error": "A user with this information already exists."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username , password=password)
            if user:
                userid = user.id
                refresh = RefreshToken.for_user(user)
                return Response({
                    'user':userid,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    
                }, status=status.HTTP_200_OK)
            else:
                return Response({'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            