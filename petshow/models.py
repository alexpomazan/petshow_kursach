from django.db import models
import os
from django.contrib.auth.models import User, AbstractUser
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
from PIL import Image

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length = 200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

# def content_user_name(reguest):
#     return auth.get_user(reguest).username

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length=200)
    comment_text = models.CharField('текст комментария' , max_length=200)
 
    def __str__(self):
        return self.author_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # img = Image.open(self.image.path)

        # if img.height >300 or img.width > 300:
        #     output_size = (150, 150)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)