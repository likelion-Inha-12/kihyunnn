from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


def api_response(data=None, message="", status=200):
    response = {
        "message": message,
        "data": data
    }
    return Response(response, status=status)


@api_view(['POST']) #FVB를 이용한 create post   
def create_post_v2(request):
    post = Post(
        title = request.data.get('title'),
        content = request.data.get('content')
    )
    post.save()

    message =  f"id : {post.pk} 포스트 생성 성공"
    return api_response(data = None, message = message, status = status.HTTP_201_CREATED)

class PostApiView(APIView): #APIView를 이용한 get, delete post

    def get_object(self, pk):
        post = get_object_or_404(Post, pk=pk)
        return post

    def get(self, request, pk):
        post = self.get_object(pk)

        postSerializer = PostSerializer(post)
        message = f"id: {post.pk}번 포스트 조회 성공"
        return api_response(data = postSerializer.data, message = message, status = status.HTTP_200_OK)
    
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        
        message = f"id: {pk}번 포스트 삭제 성공"
        return api_response(message = message, status = status.HTTP_200_OK)

from django.http import HttpResponse

def get_comment(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comment_list = post.comments.all()
        return HttpResponse(comment_list, status=200)
