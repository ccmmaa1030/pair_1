from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) # 처음 저장 했을 때 날짜
    update_at = models.DateTimeField(auto_now=True) # 매번 바꿀 때마다 갱신
