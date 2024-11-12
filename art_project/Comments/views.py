
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view


from .models import Comments
from .serializer import CommentSerializer


@api_view(['GET'])
def getComments(request):
    comments = Comments.objects.all()
    comments_data = CommentSerializer(Comments, many=True)
    return Response(comments_data.data)

@api_view(['POST'])
def addComment(request):
    comment_data = request.data
    comment = Comments(**comment_data)

    try:
        comment.save()
        comment_serialized = CommentSerializer(comment).data
        return Response({'Success' : comment_serialized})
    except Exception as e:
        return Response({'error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PATCH'])
def editComment(request):

    comment_data = request.data
    comment = Comments.objects(comment_id=comment_data["comment_id"]).first()

    if not Comment:
        return Response({"error": "Comment not found"}, status=404)

    comment_info = CommentSerializer(comment, data=request.data, partial=True)
    if comment_info.is_valid():
        comment_info.save()
        return Response(comment_info.data, status=200)
    else:
        return Response(comment_info.errors, status=400)



@api_view(['DELETE'])
def deleteComment(request):
    comment_data = request.data
    comment = Comments.objects(comment_id=comment_data["comment_id"]).first()

    if not Comment:
        return Response({"error": "Comment not found"}, status=404)

    comment.delete()

    return Response({"message": "Comment deleted"})




