from django.shortcuts import render
from . import myDef
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return render(request, 'main/index.html')
    return HttpResponse("MESSAGE")


def home(request):
    result = myDef.getResult()
    return render(request, 'main/home.html', {'result': result})


