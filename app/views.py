from django.shortcuts import  render
from django.http import HttpResponse
# def hello(request): 
#     return  HttpResponse("HELLO WOLRD")

# def goodbey(request):
#     return HttpResponse("good bey ")

# def belakh(request):
#     return HttpResponse("bea bokhoreeesh ")

def welcome(request):
    return HttpResponse("welcome to our web site master here we have some informatin about this world")
def hello (request):
    return render(request,'index.html')