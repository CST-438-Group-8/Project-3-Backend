from rest_framework import serializers
from .models import User_Post

class UserPostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user_id.username', read_only=True)
    class Meta:
        model = User_Post
        fields = ['post_id', 'user_id', 'image', 'caption','username']  