from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from qa.models import Question, Answer

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

@require_GET
def question(request, slug):
    post = get_object_or_404(Question, pk = slug)

    try:
        ans = Answer.objects.filter(question = slug)
    except:
        ans = None
    return render(request, 'question.html', {'question' : post,
                                             'answers': ans})
# Create your views here.

#def question_list(request, *args, **kwargs):
#    pass
