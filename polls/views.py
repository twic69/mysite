from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice

def index(request):
    
    questions = Question.objects.all()
    context = {
        "questions" : questions
    }
    
    return render(request, "polls/index.html", context)
    
def meme(request):
    return HttpResponse('<img src="https://i05.kanobu.ru/c/111d58588a9c0b0aa340bf240ac3056a/200x284/u.kanobu.ru/games/a044ff45-ccbd-443a-855a-232acc496c76.JPG">')

def detail(request, q_id):
    question = Question.objects.get(pk=q_id)

    context = {
        "question" : question
    }

    return render(request, "polls/detail.html", context)
def results(request, q_id):
    res = "Result for question number %s." % q_id
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for question number %s." % q_id
    return HttpResponse(res)