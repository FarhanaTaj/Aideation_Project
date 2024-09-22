from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=255)
    profile_img_path = models.ImageField(upload_to='profile_image/', null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article_thumbnail = models.ImageField(upload_to='article_thumbnails/', null=True, blank=True)

    def __str__(self):
        return self.title
