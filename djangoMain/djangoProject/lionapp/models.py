from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, default="Default Title")
    content = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True) # 처음 Post 생성시, 현재시간 저장
