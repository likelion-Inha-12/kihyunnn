from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer): #ModelSerializer를 이용한 PostSerializer
    id = serializers.IntegerField(read_only=True) #id는 자동으로 생성되므로 read_only=True로 설정
    title = serializers.CharField(max_length=100) #title은 최대 100자
    content = serializers.CharField()# content는 길이 제한 없음

    class Meta: #Meta 클래스를 이용해 Post 모델의 필드를 정의
        model = Post
        fields = ["id","title","content"]