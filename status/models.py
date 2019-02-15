from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = CurrentUserField()
    text = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    posted_at = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.posted_at = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approval=True)

    def approve_likes(self):
        return self.likes.filter(liked=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return (self.author, self.posted_at)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = CurrentUserField()
    written_at = models.DateTimeField(default=timezone.now)
    approval = models.BooleanField(default=False)

    def approve(self):
        self.approval = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return (self.author, self.written_at)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    who_liked = CurrentUserField()
    liked_at = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField()
    liked = models.BooleanField(default=False)

    def approve(self):
        self.liked = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.who_liked
