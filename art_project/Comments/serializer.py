from rest_framework import serializers
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment_id', 'comment', 'user_id', 'post_id']
