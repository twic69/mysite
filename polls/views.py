from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>ohayo</h1>")

def meme(request):
    return HttpResponse('<img src="https://media-exp1.licdn.com/dms/image/C560BAQHMnA03XDdf3w/company-logo_200_200/0/1519855918965?e=2159024400&v=beta&t=CrP5Le1mWICRcaxIGNBuajHcHGFPuyNA5C8DI339lSk">')