from rest_framework import serializers
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user_id.username', read_only=True)
    # added this line up above
    class Meta:
        model = Comments
        fields = ['comment_id', 'comment', 'user_id', 'post_id']
