# Generated by Django 4.0.6 on 2022-07-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=500, verbose_name='댓글')),
                ('like', models.BooleanField(default=False, verbose_name='좋아요')),
            ],
        ),
    ]