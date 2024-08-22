from django.shortcuts import  render
from django.http import HttpResponse

# def welcome(request):
#     return HttpResponse("welcome to our web site master here we have some informatin about this world")
# def hello (request):
#     return render(request,'index.html')
# def hello(request):
#     return render (request,'index.html')
def mahdi(request):
    return render(request,'index.html')
    