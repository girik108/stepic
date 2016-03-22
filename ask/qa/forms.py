# -*- coding: utf-8 -*-
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class AskForm(forms.Form):
    title = forms.CharField(label='Заголовок вопроса', max_length=100)
    text = forms.CharField(label='Текст вопроса', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        self.cleaned_data = super(AskForm, self).clean()
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        self.cleaned_data['author'] = self._user
        if not title and not text:
            raise forms.ValidationError('Пустые поля',code='empty fileds')
    
    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question
    
class AnswerForm(forms.Form):
    text = forms.CharField(label='Текст ответа', max_length=100)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        self.cleaned_data = super(AnswerForm, self).clean()
        text = self.cleaned_data.get('text')
        question = self.cleaned_data.get('question')
        self.cleaned_data['question'] = Question.objects.get(pk = int(question))
        
        self.cleaned_data['author'] = self._user
        if not text:
            raise forms.ValidationError('Пустые поля',code='empty text')
        
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(required = True)
    password = forms.CharField(widget = forms.PasswordInput, max_length=30)
    first_name = forms.CharField(max_length=30, required = False)
    last_name = forms.CharField(max_length=30, required = False)

    def clean(self):
        self.cleaned_data = super(SignForm, self).clean()
        password = self.cleaned_data.get('password')
        self.cleaned_data['password'] = make_password(password, salt = 'hello')
        
    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user
        
