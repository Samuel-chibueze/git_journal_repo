from rest_framework import serializers
from .models import Author, JournalModel
from django.contrib.auth.models import User



from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Author




class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'user', 'bio', 'phone_number', 'approved', 'date', 'username', 'email']
        extra_kwargs = {
            'bio': {'required': False},
            'phone_number': {'required': False},
        }

        # def create(self, validated_data):
        #     # Extract user data from validated_data
        #     user_data = validated_data.pop('user')

        #     # Check if a user with the given ID already exists in the Author model
        #     user_id = user_data.id
        #     if Author.objects.filter(user_id=user_id).exists():
        #         raise serializers.ValidationError(f"A user with that ID already exists: {user_id}")
        #     # Check if a user with the given username already exists
        #     username = user_data.username
        #     if Author.objects.filter(user__username=username).exists():
        #         raise serializers.ValidationError(f"A user with that username already exists: {username}")

        #     # Create the user
        #     user = Author.objects.create(**user_data)

        #     # Provide default values if not present in the request
        #     bio =  'Default bio'
        #     phone_number =  '000-000-0000'

        #     # Create the Author instance
        #     author = Author.objects.create(user=user, bio=bio, phone_number=phone_number)
        #     return author


class JournalSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = JournalModel
        fields = [
            'id',
            'author',
            'volume',
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
        fields = ["id",'username', 'password', 'first_name', 'last_name', 'email']

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
