from django.db import models

# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "이름" )
    kind = models.CharField(max_length = 50, verbose_name = "종류")
    content = models.TextField(verbose_name="개발툴 설명")


class Post(models.Model):
    idea = models.CharField(max_length = 50, verbose_name = "아이디어명")
    photo = models.ImageField(blank = True, upload_to = 'posts/%Y%m%d', verbose_name = "사진")
    content = models.TextField(verbose_name="아이디어 설명")
    interest = models.IntegerField(verbose_name = "아이디어 관심도")
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="tool", verbose_name="개발툴")


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    like = models.BooleanField(default=False, verbose_name="찜하기")