from django.shortcuts import render
from  django.http import HttpResponse
def hello(request): 
    return  HttpResponse("HELLO WOLRD")

def goodbey(request):
    return HttpResponse("good bey ")

def belakh(request):
    return HttpResponse("bea bokhoreeesh ")