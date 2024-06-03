from rest_framework import serializers
from .models import Author, JournalModel
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'bio', 'phone_number', 'approved', 'date', 'username','email']
        # You can include other fields you want to display, or use '__all__' and exclude 'user'
        # fields = '__all__'  # Alternatively, you can use this line and exclude the 'user' field using 'extra_kwargs'

    extra_kwargs = {
        'user': {'write_only': True}
    }
class JournalSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = JournalModel
        fields = [
            'id',
            'author',
            'title',
            'description',  # Corrected spelling here
            'file',
            'date_published',
            'rating',
            'cover_image',
            'payment_proof',
            'approved'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        return user
    

class loginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
