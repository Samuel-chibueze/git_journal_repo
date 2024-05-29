from rest_framework import serializers
from .models import Authors
from django.contrib.auth.models import User


# class JournalSerializer(serializers.ModelSerializer):
#     # author_name = serializers.SerializerMethodField()
#     # author = serializers.CharField(source='author.name', read_only=True)
#     # Publisher = serializers.CharField(source="Pubisher.name", read_only=True)
#     # Publisher_name=serializers.SerializerMethodField()
#     # Publisher_name = serializers.StringRelatedField(source='Publisher')
#     # def get_publisher_name(self, obj):
#     #     return obj.Publisher.name
    

#     class Meta:
#         model=journel_model
#         fields = ['id', 'author', 'title', 'discription', 'file', 'date_published', 'rating', 'ranking', 'Publisher', 'Publishing_house']

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Authors
        fields=["id", "name", "email", "age", "bio", "phone_number", "approved"]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def validate_email(self, value):
        # Check if any user already exists with this email.
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value

    def validate_username(self, value):
        # Check if the username is already in use.
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        return user
    

class loginSerializer(serializers.Serializer):
    username= serializers.CharField(required=True)
    password = serializers.CharField(required=True)
