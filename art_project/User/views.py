from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import User
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST'], url_path='createUser')
    def create_user(self, request):
        user_data = request.data or request.query_params
        # user = User(**user_data)

        try:
            user = User(
                username=user_data.get('username'),
                password=user_data.get('password'),
                email=user_data.get('email')
            )

            user.save()
            user_serialized = UserSerializer(user).data
            return Response({'Success' : user_serialized})
        except Exception as e:
            return Response({'Error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        
    # @api_view(['DELETE'])
    @action(detail=False, methods=['DELETE'], url_path='deleteUser')
    def delete_user(self, request):
        user_data = request.data or request.query_params

        try:
            user = User.objects.get(username=user_data['username'])
            user.delete()
            return Response({'Success' : 'User deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response({'Error' : 'User not found'}, status=status.HTTP_404_NOT_FOUND)