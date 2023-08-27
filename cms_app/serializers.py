from rest_framework import serializers
from .models import User, Post, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # Include author information
    num_likes = serializers.SerializerMethodField()  # Add this field

    class Meta:
        model = Post
        fields = '__all__'

    def get_num_likes(self, obj):
        return obj.like_set.count()  # Calculate the number of likes for the post


class LikeSerializer:
    pass