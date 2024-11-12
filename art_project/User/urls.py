from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'Users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('createUser', UserViewSet.create_user, name='Create User'),
    path('deleteUser', UserViewSet.delete_user, name='Delete User'),
    path('api-auth/', include('rest_framework.urls')),
]