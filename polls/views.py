from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

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
        "question" : question,
    }

    return render(request, "polls/detail.html", context)

def results(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question,
    }
    return render( request("polls:results", context)

def vote(request, q_id):
    choices = request.POST.getlist("choice")
    question = Question.objects.get(pk=q_id)    

    res = ""    
    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes += 1
        choice.save()
        res += "<h1>%s</h1>" % question.choice_set.get(pk=c_pk).votes

    return HttpResponseRedirect( reverse("polls:results", args=())