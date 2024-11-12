from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import User_Post
from .serializer import UserPostSerializer

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = User_Post.objects.all()
    serializer_class = UserPostSerializer

    @api_view(['POST'])
    def create_post(request):
        post_data = request.data
        post = User_Post(**post_data)

        try:
            post.save()
            post_serialized = UserPostSerializer(post).data
            return Response({'Success' : post_serialized})
        except Exception as e:
            return Response({'error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        
    @api_view(['DELETE'])
    def delete_post(request):
        post_data = request.data

        try:
            post = User_Post.objects.get(post_id=post_data['post_id'])
            post.delete()
            return Response({'Success' : 'Post deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        except User_Post.DoesNotExist:
            return Response({'Error' : 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['PATCH'])
    def edit_post(request):
        post_data = request.data

        try:
            post = User_Post.objects.get(post_id=post_data['post_id'])
        except User_Post.DoesNotExist:
            return Response({'Error' : 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'caption' in post_data:
            post.caption = post_data['caption']
            post.save()
            post_serialized = UserPostSerializer(post).data
        
            return Response({'Success': 'Post updated successfully', 'Post': post_serialized}, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Caption not provided'}, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def get_user_posts(request):
        post_data = request.data

        try:
            post = User_Post.objects.filter(user_id=post_data['user_id']).values()
            return Response({'Success' : 'Posts retrieved successfully', 'Posts' : post}, status=status.HTTP_202_ACCEPTED)
        except User_Post.DoesNotExist:
            return Response({'Error' : 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)