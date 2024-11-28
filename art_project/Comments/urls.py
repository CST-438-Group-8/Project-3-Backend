from django.contrib import admin
# from django.urls import include, path
from rest_framework.urls import path
from django.urls import path, include
# from .views import *
# from .views import getComments, deleteComment, editComment, addComment 

from .views import getComments, getUserComments, addComment, editComment, deleteComment, CommentsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Comments', CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comments/', getComments, name='Get All Comments'),
    path('userComments', getUserComments, name= 'Gets all user made comments'),
    path('delComment', deleteComment, name = 'delete Comment'),
    path('addComment', addComment, name = 'Add comment'),
    path('editComment', editComment, name= 'edit Comment'),

    path('admin/', admin.site.urls),
]