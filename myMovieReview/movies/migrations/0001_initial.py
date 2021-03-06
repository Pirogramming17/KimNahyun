# Generated by Django 4.0.6 on 2022-07-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='영화제목')),
                ('year', models.IntegerField(verbose_name='개봉연도')),
                ('director', models.CharField(max_length=50, verbose_name='감독')),
                ('actor', models.CharField(max_length=50, verbose_name='주연')),
                ('genre', models.CharField(max_length=50, verbose_name='장르')),
                ('star', models.FloatField(verbose_name='별점')),
                ('time', models.IntegerField(verbose_name='러닝타임')),
                ('review', models.CharField(max_length=50, verbose_name='리뷰내용')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
