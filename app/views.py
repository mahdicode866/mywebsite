from django.shortcuts import render
# def hello(request): 
#     return  HttpResponse("HELLO WOLRD")

# def goodbey(request):
#     return HttpResponse("good bey ")

# def belakh(request):
#     return HttpResponse("bea bokhoreeesh ")
def hello(request):
    return render(request,'index.html')