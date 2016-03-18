# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm

@require_GET
def questions_new(request, *args, **kwargs):
    page = request.GET.get('page', 1)
    question_list = Question.objects.all().order_by('-added_ad')
    paginator = Paginator(question_list, 10)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {"questions": questions})

@require_GET
def questions_pop(request, *args, **kwargs):
    page = request.GET.get('page', 1)
    question_list = Question.objects.all().order_by('-rating')
    paginator = Paginator(question_list, 10)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {"questions": questions})

#Вопрос + поле для ответа
@require_GET
def question(request, slug):
    post = get_object_or_404(Question, pk = slug)
    form = AnswerForm(initial={'question':slug})
    #form = AnswerForm(slug)
    try:
        ans = Answer.objects.filter(question = slug)
    except:
        ans = None
    return render(request, 'question.html', {'question' : post,
                                             'answers': ans, 'form':form})
#Флома для вопроса
def ask(request, *args, **kwargs):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        return render(request, 'ask_add.html', {'form': form })

