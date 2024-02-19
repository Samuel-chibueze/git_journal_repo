from rest_framework import serializers
from .models import PublishingHouse,journel_model,Publisher_model,Authors


class PublishingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=PublishingHouse
        fields="__all__"


class PublishingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publisher_model
        fields="__all__"


class JournalSerializer(serializers.ModelSerializer):
    # author_name = serializers.SerializerMethodField()
    # author = serializers.CharField(source='author.name', read_only=True)
    # Publisher = serializers.CharField(source="Pubisher.name", read_only=True)
    # Publisher_name=serializers.SerializerMethodField()
    # Publisher_name = serializers.StringRelatedField(source='Publisher')
    # def get_publisher_name(self, obj):
    #     return obj.Publisher.name
    

    class Meta:
        model=journel_model
        fields = ['id', 'author', 'title', 'content', 'date_published', 'rating', 'ranking', 'Publisher', 'Publishing_house']

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Authors
        fields=["id", "name", "email", "age", "bio", "phone_number", "approved"]