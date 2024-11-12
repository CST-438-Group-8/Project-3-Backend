from django.contrib import admin
# from django.urls import include, path
from rest_framework.urls import path
# from .views import getComments, deleteComment, editComment, addComment 
from .views import getComments, addComment, editComment, deleteComment
urlpatterns = [
    path('comments/', getComments, name='Get All Comments'),
    path('delComment', deleteComment, name = 'delete Comment'),
    path('addComment', addComment, name = 'Add comment'),
    path('editComment', editComment, name= 'edit Comment'),

    # path('admin/', admin.site.urls),
]