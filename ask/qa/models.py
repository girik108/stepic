from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):   #вопрос
    title = models.CharField(max_length = 50)  #заголовок вопроса
    text = models.TextField()                   #полный текст вопроса
    added_ad = models.DateTimeField(auto_now_add=True)           #дата добавления вопроса
    rating = models.IntegerField(default = 0)              #рейтинг вопроса (число)
    author = models.ForeignKey(User)            #автор вопроса
    likes = models.ManyToManyField(User, related_name="likelike")        #список пользователей,
                                                #поставивших "лайк"
    
    def __str__(self):
        return "Question {0} - {1}".format(self.id, self.title)


class Answer(models.Model):  #ответ
    text = models.TextField()               #текст ответа
    added_at = models.DateTimeField()       #дата добавления ответа
    question = models.ForeignKey(Question)  #вопрос, к которому относится ответ 
    author = models.ForeignKey(User)        #автор ответа

