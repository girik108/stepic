# -*- coding: utf-8 -*-
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(label='Заголовок вопроса', max_length=100)
    text = forms.CharField(label='Текст вопроса', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.__user = User.objects.get(pk = 1)
        super(AskForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        self.cleaned_data = super(AskForm, self).clean()
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        self.cleaned_data['author'] = self.__user
        if not title and not text:
            raise forms.ValidationError('Пустые поля',code='empty fileds')
    
    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question
    
class AnswerForm(forms.Form):
    text = forms.CharField(label='Текст ответа', max_length=100)
    question = forms.IntegerField(widget=forms.HiddenInput)
