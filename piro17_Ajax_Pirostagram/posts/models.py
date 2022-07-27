from django.db import models

class Comment(models.Model):
  comment = models.TextField(blank=True, max_length=500, verbose_name="댓글")
  like = models.BooleanField(default=False, verbose_name='좋아요')

