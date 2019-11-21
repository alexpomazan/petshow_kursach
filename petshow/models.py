from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# class Arcticle(models.Model):
#     article_title = models.CharField('название статьи', max_length = 200)
#     article_text = models.TextField('текст статьи')
#     pub_date = models.DateTimeField('дата публикации')
# class Comment(models.Model):
#     article = models.ForeignKey(Arcticle, on_delete = models.CASCADE)
#     author_name = models.user.username('имя автора')
#     comment_text = models.CharField('текст комментария' , max_length=200)


