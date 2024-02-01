from django.shortcuts import render
from django.http import HttpResponse
from . import myDef

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def home(request):
    result = myDef.test()
    return render(request, 'main/home.html', {'result': result})

def dict(request):
    scores = myDef.getScore()
    return render(request, 'main/score.html', {'scores': scores})


def name(request):
    result = None
    if request.method == "POST":
        form = myDef.MyForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data['value']
            result = myDef.yourName(input_data)
    else:
        form = myDef.MyForm()

    return render(request, 'main/name.html', {'result': result, 'form': form})


def news(request):
    result = None
    if request.method == "POST":
        form = myDef.MyForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data['value']
            result = myDef.news(input_data)
    else:
        form = myDef.MyForm()

    return render(request, 'main/news.html', {'result': result, 'form': form})