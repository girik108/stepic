# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length = 50)
    text = models.TextField()
    added_ad = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default = 10)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name="likelike")
    
    def __str__(self):
        return "Question {0} - {1}".format(self.id, self.title)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

