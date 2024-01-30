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


def result(request):
    result = None
    if request.method == "POST":
        form = myDef.MyForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data['value']
            result = myDef.getResult()
    else:
        form = myDef.MyForm()

    return render(request, 'main/result.html', {'result': result, 'form': form})
