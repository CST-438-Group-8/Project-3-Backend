from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import User
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @api_view(['POST'])
    def create_user(request):
        user_data = request.data
        user = User(**user_data)

        try:
            user.save()
            user_serialized = UserSerializer(user).data
            return Response({'Success' : user_serialized})
        except Exception as e:
            return Response({'Error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        
    @api_view(['DELETE'])
    def delete_user(request):
        user_data = request.data 

        try:
            user = User.objects.get(username=user_data['username'])
            user.delete()
            return Response({'Success' : 'User deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response({'Error' : 'User not found'}, status=status.HTTP_404_NOT_FOUND)