from django.shortcuts import HttpResponse, render

# Create your views here.

def myfun(request):
    return render(request,"my.html")