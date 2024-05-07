from django.db import models

class Member(models.Model): # Member 모델 정의
    name = models.CharField(max_length=20) # 최대 20자까지 저장 가능
    email = models.EmailField(unique=True) # 이메일 형식으로 저장, 중복 불가능

class Post(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE,null=True, related_name='posts') # Member 모델과 1:N 관계 설정
    title = models.CharField(max_length=50, default="Default Title") # 최대 50자까지 저장 가능
    content = models.TextField(null=True, blank=True) # 글자수 제한 없음
    create_at = models.DateTimeField(auto_now_add=True) # 처음 Post 생성시, 현재시간 저장

class Comment(models.Model): # Comment 모델 정의
    author = models.ForeignKey(Member, on_delete=models.CASCADE,null=True, related_name='comments') # Member 모델과 1:N 관계 설정
    content = models.CharField(max_length = 200, null = True, blank = True)# 최대 200자까지 저장 가능
    post_id = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name="comments") # Post 모델과 1:N 관계 설정

    def __str__(self):
        return self.content

class MemberPost(models.Model): # MemberPost 모델 정의 일대다, 다대일 관계
    member = models.ForeignKey(Member, on_delete=models.CASCADE) # Member 모델과 1:N 관계 설정
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # Post 모델과 1:N 관계 설정


