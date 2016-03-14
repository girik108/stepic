from django.db import models
from django.contrib.auth.models import User# as DjUser

# Create your models here.

#class User(DjUser):
#    def __init__(self):
#        super.__init__(self)


class Question(models.Model):   #вопрос
    title = models.CharField(max_length = 50)  #заголовок вопроса
    text = models.TextField()                   #полный текст вопроса
    added_ad = models.DateTimeField()           #дата добавления вопроса
    rating = models.IntegerField(default = 0)              #рейтинг вопроса (число)
    author = models.ForeignKey(User)            #автор вопроса
    likes = models.ManyToManyField(User, related_name="likelike")        #список пользователей,
                                                #поставивших "лайк"
#    class Meta:
#        db_table

class Answer(models.Model):  #ответ
    text = models.TextField()               #текст ответа
    added_at = models.DateTimeField()       #дата добавления ответа
    question = models.ForeignKey(Question)  #вопрос, к которому относится ответ 
    author = models.ForeignKey(User)        #автор ответа

