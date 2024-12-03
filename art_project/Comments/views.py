
# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action


from .models import Comments
from .serializer import CommentSerializer
from User.models import User
from User_post.models import User_Post



class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

@api_view(['GET'])
def getComments(request):
    comments = Comments.objects.all()
    comments_data = CommentSerializer(Comments, many=True)
    return Response(comments_data.data)



@api_view(['GET'])
def getUserComments(request):
    post_id = request.GET.get('post_id')
    comments = Comments.objects.filter(post_id = post_id)

    if not post_id:
        return Response({"error": "post_id required"}, status=status.HTTP_404_NOT_FOUND)
    print(comments)

    comments_data = CommentSerializer(comments, many = True)
    return Response(comments_data.data)

# @api_view(['POST'])
# def addComment(request):
#     comment_data = request.data
#     comment = Comments(**comment_data)

#     try:
#         comment.save()
#         comment_serialized = CommentSerializer(comment).data
#         return Response({'Success' : comment_serialized})
#     except Exception as e:
#         return Response({'error' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def addComment(request):
    comment = request.data.get('comment')
    user_id = request.data.get('user_id')
    post_id = request.data.get('post_id')

    if not comment or not user_id or not post_id:
        return Response(
            {"error": "comment, user_id, and post_id are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = User.objects.get(pk=user_id)
        post = User_Post.objects.get(pk=post_id)

    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except User_Post.DoesNotExist:
        return Response({"error": "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)

    comment_object = Comments.objects.create(
        comment=comment,
        user_id=user,
        post_id=post,
    )

    serializer = CommentSerializer(comment_object)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



# @api_view(['PATCH'])
# def editComment(request):

#     comment_data = request.data
#     comment = Comments.objects(comment_id=comment_data["comment_id"]).first()

#     if not Comment:
#         return Response({"error": "Comment not found"}, status=404)

#     comment_info = CommentSerializer(comment, data=request.data, partial=True)
#     if comment_info.is_valid():
#         comment_info.save()
#         return Response(comment_info.data, status=200)
#     else:
#         return Response(comment_info.errors, status=400)
@api_view(['PATCH'])
def editComment(request):
    comment_id = request.data.get("comment_id")
    
    if not comment_id:
        return Response({"error": "comment_id is required"}, status=status.HTTP_400_BAD_REQUEST)

    comment = get_object_or_404(Comments, pk=comment_id)


    serializer = CommentSerializer(comment, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def deleteComment(request):
#     comment_data = request.data
#     comment = Comments.objects(comment_id=comment_data["comment_id"]).first()

#     if not Comment:
#         return Response({"error": "Comment not found"}, status=404)

#     comment.delete()

#     return Response({"message": "Comment deleted"})
@api_view(['DELETE'])
def deleteComment(request):
    comment_id = request.data.get('comment_id')

    if not comment_id:
        return Response(
            {"error": "comment_id is required for deletion"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    comment = get_object_or_404(Comments, pk=comment_id)
    comment.delete()
    return Response({"message": f"Comment {comment_id} deleted"}, status=status.HTTP_200_OK)



