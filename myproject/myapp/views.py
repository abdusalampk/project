from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import mentor

# Create your views here.

def home(request):
    obj=place.objects.all()
    objj=mentor.objects.all()
    return render(request,"index.html",{'result':obj,'res':objj})
#def demo(request):
    #return HttpResponse("hello world")