from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'filterdesigner/index.html')

def RCLowPassDetail(request):
    return HttpResponse("This will be RC Low pass")