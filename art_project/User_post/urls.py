from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'posts', UserPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('createPost', UserPostViewSet.create_post, name='Create Post'),
    # path('deletePost', UserPostViewSet.delete_post, name='Delete Post'),
    # path('editPost', UserPostViewSet.edit_post, name='Edit Post'),
    # path('getUserPosts', UserPostViewSet.get_user_posts, name='Get User Posts'),
    path('api-auth/', include('rest_framework.urls')),
]