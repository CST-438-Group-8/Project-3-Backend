from rest_framework import serializers
from .models import User_post

class User_Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_post
        fields = ['comment_id', 'comment', 'user_id', 'post_id']
