from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import User_Post, User
from .serializer import UserPostSerializer

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = User_Post.objects.all()
    serializer_class = UserPostSerializer

    # @api_view(['POST'])
    @action(detail=False, methods=['POST'], url_path='createPost')
    def create_post(self, request):
        post_data = request.data or request.query_params
        # post = User_Post(**post_data)

        try:
            user = User.objects.get(user_id=post_data.get('user_id'))
            
            post = User_Post(
                user_id=user,
                image=post_data.get('image'),
                caption=post_data.get('caption')
            )

            post.save()
            post_serialized = UserPostSerializer(post).data
            return Response({'Success' : 'Post created successfully', 'Post' : post_serialized}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'Error' : 'User does not exist'})
        except Exception as e:
            return Response({'Error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        
    # @api_view(['DELETE'])
    @action(detail=False, methods=['DELETE'], url_path='deletePost')
    def delete_post(self, request):
        post_data = request.data or request.query_params

        try:
            post = User_Post.objects.get(post_id=post_data['post_id'])
            post.delete()
            return Response({'Success' : 'Post deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        except User_Post.DoesNotExist:
            return Response({'Error' : 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # @api_view(['PATCH'])
    @action(detail=False, methods=['PATCH'], url_path='editPost')
    def edit_post(self, request):
        post_data = request.data or request.query_params

        try:
            post = User_Post.objects.get(post_id=post_data['post_id'])
        except User_Post.DoesNotExist:
            return Response({'Error' : 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'caption' in post_data:
            post.caption = post_data['caption']
            post.save()
            post_serialized = UserPostSerializer(post).data
        
            return Response({'Success': 'Post updated successfully', 'Post': post_serialized}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Error': 'Caption not provided'}, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['GET'])
    @action(detail=False, methods=['GET'], url_path='getUserPosts')
    def get_user_posts(self, request):
        post_data = request.data or request.query_params

        try:
            user = User.objects.get(user_id=post_data.get('user_id'))
            post = User_Post.objects.filter(user_id=user).values()
            return Response({'Success' : 'Posts retrieved successfully', 'Posts' : post}, status=status.HTTP_202_ACCEPTED)
        except User_Post.DoesNotExist:
            return Response({'Error' : 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)