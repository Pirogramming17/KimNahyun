from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "영화제목")
    year = models.IntegerField(verbose_name = "개봉년도")
    director = models.CharField(max_length = 50, verbose_name = "감독")
    actor = models.CharField(max_length = 50, verbose_name = "주연")
    genre = models.CharField(max_length = 50, verbose_name = "장르")
    star = models.FloatField(max_length = 5, verbose_name = "별점")
    time = models.IntegerField(verbose_name = "러닝타임")
    review = models.CharField(max_length = 500, verbose_name = "리뷰내용")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    

