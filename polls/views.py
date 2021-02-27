from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice

def index(request):
    q_all = Question.objects.all()
    res = "<ol>"

    for q in q_all:
        res += "<li>%s</li>" % q.text
    res += "</ol>"

    return HttpResponse(res)

    
def meme(request):
    return HttpResponse('<img src="https://media-exp1.licdn.com/dms/image/C560BAQHMnA03XDdf3w/company-logo_200_200/0/1519855918965?e=2159024400&v=beta&t=CrP5Le1mWICRcaxIGNBuajHcHGFPuyNA5C8DI339lSk">')

def detail(request, q_id):
    res = "Question number %s." % q_id
    return HttpResponse(res)

def results(request, q_id):
    res = "Result for question number %s." % q_id
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for question number %s." % q_id
    return HttpResponse(res)